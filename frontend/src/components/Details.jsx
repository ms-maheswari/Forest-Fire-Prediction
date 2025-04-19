import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const Details = () => {
  const { id } = useParams();
  const [forest, setForest] = useState(null);
  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    axios.get(`http://localhost:5000/api/forest/${id}`)
      .then(res => setForest(res.data))
      .catch(err => console.error('Error:', err));
  }, [id]);

  const handlePredict = () => {
    setLoading(true);
    axios.post(`http://localhost:5000/api/predict`, { forest_id: id })
      .then(res => setPrediction(res.data))
      .catch(err => console.error('Prediction Error:', err))
      .finally(() => setLoading(false));
  };

  
  if (!forest) {
    return <div className="flex justify-center items-center h-screen text-gray-500 text-xl">Loading forest details...</div>;
  }

  return (
    <div className="p-6 max-w-7xl mx-auto">
      {/* Header */}
      <div className="mb-8 p-6 rounded-2xl bg-gradient-to-r from-green-200 via-blue-100 to-green-200 shadow-md text-center">
        <h1 className="text-4xl font-extrabold text-green-900 mb-1">{forest.name}</h1>
        <p className="text-sm text-gray-700">{forest.location.district || forest.location.region}</p>
      </div>

      {/* Weather & Vegetation */}
      <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
        {/* Weather Card */}
        <div className="bg-white/60 backdrop-blur-lg p-6 rounded-xl border border-blue-100 shadow-md hover:shadow-xl transition">
          <h2 className="text-2xl font-semibold text-blue-900 mb-4">🌤 Weather Overview</h2>
          <ul className="space-y-2 text-gray-700">
            <li>🌡 <strong>Temperature:</strong> {forest.weather.temperature} °C</li>
            <li>💧 <strong>Humidity:</strong> {forest.weather.humidity} %</li>
            <li>💨 <strong>Wind Speed:</strong> {forest.weather.wind_speed} m/s</li>
            <li>☁️ <strong>Cloud Coverage:</strong> {forest.weather.cloud_coverage} %</li>
            <li>🌧 <strong>Rainfall:</strong> {forest.weather.rainfall} mm</li>
          </ul>
        </div>

        {/* Vegetation Card */}
        <div className="bg-white/60 backdrop-blur-lg p-6 rounded-xl border border-green-100 shadow-md hover:shadow-xl transition">
          <h2 className="text-2xl font-semibold text-green-900 mb-4">🌿 Vegetation Composition</h2>
          <ul className="space-y-2 text-gray-700">
            {forest.vegetation.map((v, i) => (
              <li key={i}>🌱 <strong>{v.type}:</strong> {v.percentage}%</li>
            ))}
          </ul>
        </div>
      </div>

      {/* Predict Button */}
      <div className="flex justify-center mt-10">
    

        <button
          onClick={handlePredict}
          disabled={loading}
          className={`px-8 py-3 rounded-full text-lg font-semibold transition-all duration-300 shadow-md ${
            loading
              ? 'bg-gray-400 text-white cursor-not-allowed'
              : 'bg-gradient-to-r from-red-500 via-orange-500 to-yellow-400 text-white hover:scale-105'
          }`}
        >
          {loading ? 'Predicting...' : '🔥 Predict Forest Fire Risk'}
        </button>
      </div>

      {/* Prediction Results */}
      {prediction && (
        <div className="mt-12 p-6 bg-orange-50 border-l-4 border-orange-400 rounded-xl shadow-md">
          <h3 className="text-2xl font-bold text-red-700 mb-2">🔥 Fire Risk Level: {prediction.risk_level}</h3>
          <p className="text-gray-800 mb-1">🔥 <strong>Probability:</strong> {prediction.probability}%</p>
          {/* <p className="text-gray-800 mb-4">🌿 <strong>Vegetation Risk:</strong> {prediction.vegetation_risk}</p> */}

          <h4 className="text-lg font-semibold text-gray-700 mb-2">📊 Features Used</h4>
          <ul className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-2 text-gray-700 text-lg">
            <li>🌡 Temperature: {prediction.features[0]} °C</li>
            <li>💧 Humidity: {prediction.features[1]} %</li>
            <li>💨 Wind Speed: {prediction.features[2]} m/s</li>
            <li>🌿 Vegetation Risk: {prediction.features[3]}</li>
            <li>⛰ Elevation: {prediction.features[4]} m</li>
            <li>🌱 Biomass: {prediction.features[5]} t/ha</li>
            <li>☁️ Cloud Coverage: {prediction.features[6]} %</li>
            <li>🌧 Rainfall: {prediction.features[7]} mm</li>
            <li>🔥 Dryness Index: {prediction.features[8].toFixed(2)}</li>
            {/* <li>📅 Month: {prediction.features[9]}</li> */}
          </ul>
        </div>
      )}
    </div>
  );
};

export default Details;
