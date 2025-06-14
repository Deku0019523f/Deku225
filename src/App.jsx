import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import Quiz from './components/Quiz';
import Login from './components/Login';
import Classement from './components/Classement';
import Admin from './components/Admin';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/quiz/:niveau" element={<Quiz />} />
        <Route path="/login" element={<Login />} />
        <Route path="/classement" element={<Classement />} />
        <Route path="/admin" element={<Admin />} />
      </Routes>
    </Router>
  );
}