import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Details from './components/Details';

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/forest/:id" element={<Details />} />
    </Routes>
  );
};

export default App;
