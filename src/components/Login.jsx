import React, { useState } from 'react';
import { supabase } from '../supabase';

export default function Login() {
  const [email, setEmail] = useState('');
  const [sent, setSent] = useState(false);

  const handleLogin = async () => {
    const { error } = await supabase.auth.signInWithOtp({ email });
    if (!error) setSent(true);
  };

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Connexion</h2>
      {!sent ? (
        <>
          <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} placeholder="Votre email" className="border p-2 mb-2 w-full" />
          <button onClick={handleLogin} className="bg-blue-500 text-white px-4 py-2">Envoyer le lien magique</button>
        </>
      ) : (
        <p>Vérifie ta boîte mail 📩</p>
      )}
    </div>
  );
}