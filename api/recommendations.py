from flask import Blueprint, jsonify
from flask_login import login_required, current_user

# Function to generate personalized recommendations based on user ID
def get_personalized_recommendations(user_id):
    # Sample recommendations (replace with your own recommendation logic)
    recommendations = [
        {'title': 'Healthy Eating Habits', 'description': 'Eat a balanced diet rich in fruits and vegetables.'},
        {'title': 'Regular Exercise', 'description': 'Engage in physical activity for at least 30 minutes a day.'},
        {'title': 'Adequate Sleep', 'description': 'Ensure you get 7-9 hours of quality sleep each night.'}
    ]
    
    return recommendations

# Blueprint for recommendations routes
recommendations_bp = Blueprint('recommendations', __name__)

# Route to get personalized recommendations
@recommendations_bp.route('/recommendations', methods=['GET'])
@login_required  # Require the user to be logged in
def get_recommendations():
    # Get the ID of the current logged-in user
    user_id = current_user.get_id()

    # Get personalized recommendations for the user
    recommendations = get_personalized_recommendations(user_id)

    # Return recommendations as JSON response
    return jsonify(recommendations), 200
