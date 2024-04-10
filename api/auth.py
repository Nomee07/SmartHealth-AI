from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from backend.models import db, User

# Create a blueprint for authentication routes
auth_bp = Blueprint('auth', __name__)

# Route for user registration
@auth_bp.route('/register', methods=['POST'])
def register():
    # Retrieve JSON data from request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Generate hashed password
    hashed_password = generate_password_hash(password)

    # Create a new user object
    new_user = User(username=username, password=hashed_password)

    # Add new user to the database
    db.session.add(new_user)
    db.session.commit()

    # Return success message
    return jsonify({'message': 'User registered successfully'}), 201

# Route for user login
@auth_bp.route('/login', methods=['POST'])
def login():
    # Retrieve JSON data from request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    # Check if username and password are provided
    if not username or not password:
        return jsonify({'error': 'Username and password are required'}), 400

    # Query user from the database by username
    user = User.query.filter_by(username=username).first()

    # Check if user exists and password is correct
    if not user or not check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid username or password'}), 401

    # Return success message
    return jsonify({'message': 'Login successful'}), 200
