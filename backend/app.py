from flask import Flask
from backend.auth import auth_bp  # Importing authentication blueprint
from backend.models import db  # Importing database instance


app = Flask(__name__)  # Creating Flask application instance

# Configuring SQLAlchemy settings
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initializing SQLAlchemy with the Flask application instance
db.init_app(app)

# Registering the authentication blueprint with the Flask application
app.register_blueprint(auth_bp)

# Route for the home page
@app.route('/')
def index():
    return 'Welcome to SmartHealth AI!'  # Response for the home page

# Running the Flask application
if __name__ == '__main__':
    app.run(debug=True)  # Running the app in debug mode if this script is executed directly
