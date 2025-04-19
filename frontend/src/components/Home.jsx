import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Home = () => {
  const [forests, setForests] = useState([]);
  const [search, setSearch] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    axios.get('http://localhost:5000/api/forests')
      .then(res => setForests(res.data))
      .catch(err => console.error('Error fetching forests:', err));
  }, []);

  const filteredForests = forests.filter(f =>
    f.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="bg-gradient-to-br from-green-50 to-green-100 min-h-screen py-10 px-4">
      <div className="max-w-7xl mx-auto">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-4xl font-extrabold text-green-800">🌲  Forest Fire Prediction</h1>
          
        </div>

        {/* Search Bar */}
        <div className="mb-8">
          <input
            type="text"
            placeholder="🔍 Search forest..."
            value={search}
            onChange={e => setSearch(e.target.value)}
            className="w-full md:w-1/2 px-5 py-3 rounded-full border border-green-300 shadow-sm focus:outline-none focus:ring-2 focus:ring-green-500"
          />
        </div>

        {/* Forest Cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8">
          {filteredForests.map(forest => (
            <div
              key={forest.id}
              className="bg-white rounded-3xl shadow-md p-6 hover:shadow-xl transition transform hover:-translate-y-1 cursor-pointer"
            >
              <h2 className="text-2xl font-semibold text-green-700 mb-1">{forest.name}</h2>
              <p className="text-sm text-gray-600">📍 {forest.location.district || forest.location.region}</p>
              <p className="text-sm text-gray-600">🗺️ Area: {forest.characteristics.area} sq.km</p>

              {/* Vegetation Tags (optional if available) */}
              {forest.vegetation && forest.vegetation.length > 0 && (
                <div className="flex flex-wrap gap-2 mt-3">
                  {forest.vegetation.slice(0, 2).map((v, i) => (
                    <span
                      key={i}
                      className="px-2 py-1 text-xs bg-green-100 text-green-800 rounded-full"
                    >
                      🌿 {v.type}
                    </span>
                  ))}
                </div>
              )}

              <button
                onClick={() => navigate(`/forest/${forest.id}?forestName=${encodeURIComponent(forest.name)}`)}

                // onClick={() => navigate(`/forest/${forest.id}`)}
                className="mt-6 w-full px-4 py-2 bg-green-600 text-white rounded-lg font-medium hover:bg-green-700 transition"
              >
                🔎 View Details
              </button>
            </div>
          ))}
        </div>

        {/* No Results Message */}
        {filteredForests.length === 0 && (
          <p className="mt-10 text-center text-gray-500 text-lg">No forests match your search. 🌱</p>
        )}
      </div>
    </div>
  );
};

export default Home;
