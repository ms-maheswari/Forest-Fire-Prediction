import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import joblib
from forests import FORESTS
import os

def calculate_vegetation_risk(vegetation):
    return sum(v['percentage'] * v['fire_risk_factor'] for v in vegetation) / 100
def generate_training_data():
    samples = []

    for forest in FORESTS:
        veg_risk = calculate_vegetation_risk(forest['characteristics']['vegetation'])
        elevation = forest['location']['elevation']
        biomass = forest['characteristics']['avg_biomass']

        # Generate 500 low-risk and 500 high-risk samples
        for _ in range(500):
            # 🔵 Low fire risk
            temp = np.random.uniform(10, 25)
            humidity = np.random.uniform(60, 90)
            wind = np.random.uniform(0, 5)
            rainfall = np.random.uniform(10, 50)
            cloud_coverage = np.random.uniform(30, 100)
            month = np.random.randint(1, 13)
            dryness_index = (100 - humidity) + (wind * 0.8) - (0.3 * rainfall)
            samples.append([
                temp, humidity, wind, veg_risk, elevation, biomass,
                cloud_coverage, rainfall, dryness_index, month, 0
            ])

        for _ in range(500):
            # 🔴 High fire risk
            temp = np.random.uniform(35, 45)
            humidity = np.random.uniform(10, 30)
            wind = np.random.uniform(15, 40)
            rainfall = np.random.uniform(0, 2)
            cloud_coverage = np.random.uniform(0, 20)
            month = np.random.randint(3, 6)  # Summer months
            dryness_index = (100 - humidity) + (wind * 0.8) - (0.3 * rainfall)
            samples.append([
                temp, humidity, wind, veg_risk, elevation, biomass,
                cloud_coverage, rainfall, dryness_index, month, 1
            ])

    columns = [
        'temperature', 'humidity', 'wind_speed',
        'vegetation_risk', 'elevation', 'biomass',
        'cloud_coverage', 'rainfall', 'dryness_index',
        'month', 'fire_risk'
    ]
    return pd.DataFrame(samples, columns=columns)



def train_universal_model():
    print("Training universal model with 10 features...")
    df = generate_training_data()

    X = df.drop('fire_risk', axis=1)
    y = df['fire_risk']

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=15,
        class_weight='balanced',
        random_state=42
    )
    model.fit(X, y)

    os.makedirs('trained_models', exist_ok=True)
    joblib.dump({
        'model': model,
        'feature_names': list(X.columns),
        'training_date': pd.Timestamp.now().strftime('%Y-%m-%d')
    }, 'trained_models/universal_model.joblib')
    print(df['fire_risk'].value_counts())

    print(f"✅ Model trained with accuracy: {model.score(X, y):.2f}")
    print("📁 Model saved to trained_models/universal_model.joblib")

if __name__ == '__main__':
    train_universal_model()
