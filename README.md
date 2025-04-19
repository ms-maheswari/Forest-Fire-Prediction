# 🌲🔥 Forest Fire Prediction System

An AI-powered application that predicts the risk of forest fires using real-time weather and vegetation data, with intelligent visualizations and alert systems. Built using React (frontend), Flask (backend), Power BI (dashboard), and a trained Random Forest model for accurate fire risk classification.



## 📌 Project Overview

This system helps in early detection and risk assessment of forest fires, especially for forests in Tamil Nadu and worldwide. By fetching live weather data and evaluating vegetation types, the system uses machine learning to calculate the likelihood of a fire occurring and immediately sends alerts for high-risk zones.


## 🎯 Key Features

- 🔍 **Fire Risk Prediction** using a trained Random Forest model  
- 🌦 **Live Weather Data** from OpenWeatherMap API  
- 🌿 **Vegetation Analysis** with percentage distribution  
- 📊 **Power BI Dashboard** for dynamic weather and vegetation charts  
- 📧 **Automated Email Alerts** for high-risk predictions  
- 🔐 **Secure API & Email Integration** using `.env`  



## 🧠 Machine Learning Model

### 📚 Algorithm Used

🎲 **Random Forest Classifier**  
An ensemble learning algorithm that builds multiple decision trees and merges their outputs to get more accurate and stable predictions. Each tree casts a vote, and the majority determines the final output.

- Resistant to overfitting  
- Handles both numerical and categorical data  
- Performs well on high-dimensional datasets  
- Used **GridSearchCV** for hyperparameter tuning

### 🔍 Model Details

- **Model Path**: `models/high_accuracy_model.joblib`
- **Features Used**:
  - Temperature
  - Humidity
  - Wind Speed
  - Dryness Index
  - Temp-Humidity Index *(engineered)*
  - Wind-Dryness Factor *(engineered)*
  - Danger Score *(engineered)*
- **Prediction Output**: 🔥 Risk Level  
  - Low 🔵  
  - Moderate 🟡  
  - High 🔴  



## 🛠 Tech Stack

| Component       | Technology                    |
|----------------|-------------------------------|
| Frontend       | React, Tailwind CSS           |
| Backend        | Flask, Python, dotenv         |
| ML Model       | Scikit-learn (Random Forest)  |
| Visualization  | Power BI (Push Dataset)       |
| APIs Used      | OpenWeatherMap API            |
| Email Alerts   | Gmail SMTP + Python Email     |



## 🔐 Environment Variables

Create a `.env` file inside the `backend/` directory:

```bash
# OpenWeatherMap API
OPENWEATHER_API_KEY=your_openweather_api_key

# Email Alerts
From=your_email@gmail.com
To=recipient_email@gmail.com
EMAIL_PASSWORD=your_gmail_app_password

# Power BI (Optional)
powerbi_url=your_powerbi_streaming_key
```

## Getting Started

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py
```

### Frontend
```bash
cd frontend
npm install
npm start
```
