from flask import Flask, request, jsonify
import joblib
import numpy as np
from forests import FORESTS
import smtplib
from email.message import EmailMessage
import requests
from datetime import datetime
from flask_cors import CORS
import time
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
CORS(app)

# Load model
model_data = joblib.load('trained_models/universal_model.joblib')
model = model_data['model']

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
POWERBI_STREAM_URL = os.getenv("powerbi_url")

# Track last request time to prevent duplicates
last_request_time = {}


def get_realtime_weather(lat, lon):
    url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric'
    response = requests.get(url)
    data = response.json()

    try:
        return {
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed'],
            'cloud_coverage': data.get('clouds', {}).get('all', 0),
            'rainfall': data.get('rain', {}).get('1h', 0)
        }
    except KeyError as e:
        print(f"Missing key in API response: {e}")
        return {
            'temperature': 30,
            'humidity': 50,
            'wind_speed': 5,
            'cloud_coverage': 50,
            'rainfall': 0
        }

def calculate_vegetation_risk(vegetation):
    return sum(v['percentage'] * v['fire_risk_factor'] for v in vegetation) / 100

def send_email_alert(forest_name, risk_level, proba):
    msg = EmailMessage()
    msg['Subject'] = f'🔥 Forest Fire Alert: {risk_level} Risk in {forest_name}'
    msg['From'] = os.getenv("From")
    msg['To'] = os.getenv("To")

    msg.set_content(f'''
    Alert from Forest Fire Prediction System:

    Forest: {forest_name}
    Fire Risk Level: {risk_level}
    Probability: {round(proba * 100, 1)}%

    Please take immediate action if necessary.
    ''')

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("From"), os.getenv("EMAIL_PASSWORD"))
        smtp.send_message(msg)


def push_to_powerbi(forest_name, temperature, humidity, wind_speed, vegetation):
    rows = []
    timestamp = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    
    rows.append({
    "forest_name": forest_name,
    "temperature": float(temperature),
    "humidity": float(humidity),
    "wind_speed": float(wind_speed),
    "vegetation_type": "All",
    "vegetation_percentage": 0
})
    for v in vegetation:
        rows.append({
            "forest_name": forest_name,
            "temperature": 0,
            "humidity": 0,
            "wind_speed": 0,
            "vegetation_type": v['type'],
            "vegetation_percentage": float(v['percentage']),
            "timestamp": timestamp
        })

    try:
        response = requests.post(
            POWERBI_STREAM_URL,
            json=rows,
            headers={"Content-Type": "application/json"},
            timeout=3
        )
        print(f"Power BI Response: {response.status_code} - {response.text}")
    except Exception as e:
        print(f"Power BI Error: {str(e)}")


@app.route('/')
def home():
    return "Forest Fire Prediction System API"

@app.route('/api/forests', methods=['GET'])
def get_forests():
    simplified = [{
        'id': f['id'],
        'name': f['name'],
        'location': f['location'],
        'characteristics': {
            'area': f['characteristics']['area']
        }
    } for f in FORESTS]
    return jsonify(simplified)

@app.route('/api/forest/<int:forest_id>', methods=['GET'])
def get_forest_details(forest_id):
    # Deduplication check - ignore same request within 2 seconds
    current_time = time.time()
    if forest_id in last_request_time and (current_time - last_request_time[forest_id]) < 2:
        return jsonify({'warning': 'Duplicate request ignored'}), 429
    
    last_request_time[forest_id] = current_time

    forest = next((f for f in FORESTS if f['id'] == forest_id), None)
    if not forest:
        return jsonify({'error': 'Forest not found'}), 404

    weather = get_realtime_weather(
        forest['location']['latitude'],
        forest['location']['longitude']
    )

    veg_risk = calculate_vegetation_risk(forest['characteristics']['vegetation'])

    # Push data to Power BI
    push_to_powerbi(
        forest['name'],
        weather['temperature'],
        weather['humidity'],
        weather['wind_speed'],
        forest['characteristics']['vegetation']
    )

    return jsonify({
        'id': forest['id'],
        'name': forest['name'],
        'location': forest['location'],
        'characteristics': {
            'area': forest['characteristics']['area']
        },
        'vegetation': forest['characteristics']['vegetation'],
        'avg_biomass': forest['characteristics']['avg_biomass'],
        'weather': weather,
        'vegetation_risk': veg_risk
    })

@app.route('/api/predict', methods=['POST'])
def predict_fire():
    data = request.json
    forest_id = int(data.get('forest_id'))

    forest = next((f for f in FORESTS if f['id'] == forest_id), None)
    if not forest:
        return jsonify({'error': 'Forest not found'}), 404

    weather = get_realtime_weather(
        forest['location']['latitude'],
        forest['location']['longitude']
    )

    temperature = weather.get('temperature', 30)
    humidity = weather.get('humidity', 50)
    wind_speed = weather.get('wind_speed', 10)
    cloud_coverage = weather.get('cloud_coverage', 50)
    rainfall = weather.get('rainfall', 5)
    dryness_index = (100 - humidity) + temperature + wind_speed
    month = datetime.now().month

    veg_risk = calculate_vegetation_risk(forest['characteristics']['vegetation'])
    elevation = forest['location']['elevation']
    biomass = forest['characteristics']['avg_biomass']

    features = np.array([[temperature, humidity, wind_speed, veg_risk, elevation,
                          biomass, cloud_coverage, rainfall, dryness_index, month]])

    proba = model.predict_proba(features)[0][1]

    risk_level = (
        'Extreme' if proba > 0.5 else
        'High' if proba > 0.35 else
        'Moderate' if proba > 0.2 else
        'Low'
    )

    # Push to Power BI
    push_to_powerbi(
        forest['name'],
        temperature,
        humidity,
        wind_speed,
        forest['characteristics']['vegetation']
    )

    if risk_level in ['Extreme', 'High']:
        send_email_alert(forest['name'], risk_level, proba)

    return jsonify({
        'forest_id': forest_id,
        'risk_level': risk_level,
        'probability': round(proba * 100, 2),
        'vegetation_risk': round(veg_risk, 2),
        'features': features.tolist()[0]
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)