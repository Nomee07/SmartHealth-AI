import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>SmartHealth AI</h1>
        <div>
          <h2>Login</h2>
          <input type="text" placeholder="Username" />
          <input type="password" placeholder="Password" />
          <button>Login</button>
        </div>
        <div>
          <h2>Register</h2>
          <input type="text" placeholder="Username" />
          <input type="password" placeholder="Password" />
          <button>Register</button>
        </div>
      </header>
    </div>
  );
}

export default App;
