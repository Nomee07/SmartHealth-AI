from flask import Blueprint, jsonify
from flask_login import login_required, current_user


def get_personalized_recommendations(user_id):
    recommendations = [
        {'title': 'Healthy Eating Habits', 'description': 'Eat a balanced diet rich in fruits and vegetables.'},
        {'title': 'Regular Exercise', 'description': 'Engage in physical activity for at least 30 minutes a day.'},
        {'title': 'Adequate Sleep', 'description': 'Ensure you get 7-9 hours of quality sleep each night.'}
    ]
    
    return recommendations


recommendations_bp = Blueprint('recommendations', __name__)

@recommendations_bp.route('/recommendations', methods=['GET'])
@login_required
def get_recommendations():
    user_id = current_user.get_id()

    recommendations = get_personalized_recommendations(user_id)

    return jsonify(recommendations), 200
