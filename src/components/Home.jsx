import React from 'react';
import { Link } from 'react-router-dom';

export default function Home() {
  return (
    <div className="p-4 text-center">
      <h1 className="text-2xl font-bold mb-4">Bienvenue sur Quiz Manga</h1>
      <Link to="/login" className="text-blue-500 underline">Commencer</Link>
    </div>
  );
}
