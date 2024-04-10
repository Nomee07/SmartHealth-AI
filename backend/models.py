from flask_sqlalchemy import SQLAlchemy

# Create a SQLAlchemy instance
db = SQLAlchemy()

# Define the User model, which represents a user entity in the database
class User(db.Model):
    # Define the columns of the User table
    id = db.Column(db.Integer, primary_key=True)  # Primary key column for unique identification
    username = db.Column(db.String(50), unique=True, nullable=False)  # Username column, unique and not nullable
    password = db.Column(db.String(100), nullable=False)  # Password column, not nullable
