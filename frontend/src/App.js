import React from 'react'; // Importing React library
import './App.css'; // Importing CSS styles from external file

// Functional component named App
function App() {
  return (
    <div className="App"> {/* Root div with class name "App" */}
      <header className="App-header"> {/* Header section with class name "App-header" */}
        <h1>SmartHealth AI</h1> {/* Main title */}
        <div> {/* Login section */}
          <h2>Login</h2> {/* Subtitle for login section */}
          <input type="text" placeholder="Username" /> {/* Input field for username */}
          <input type="password" placeholder="Password" /> {/* Input field for password */}
          <button>Login</button> {/* Login button */}
        </div>
        <div> {/* Register section */}
          <h2>Register</h2> {/* Subtitle for register section */}
          <input type="text" placeholder="Username" /> {/* Input field for username */}
          <input type="password" placeholder="Password" /> {/* Input field for password */}
          <button>Register</button> {/* Register button */}
        </div>
      </header>
    </div>
  );
}

export default App; // Exporting the App component
