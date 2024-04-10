import os

# Get the absolute path of the directory where this Python script resides
basedir = os.path.abspath(os.path.dirname(__file__))

# Flask configuration options

# Secret key used by Flask to securely sign session cookies and other security-related functionalities
SECRET_KEY = 'your_secret_key'

# Database URI for SQLAlchemy to connect to
# In this case, it's set to use SQLite, and the database file will be located in the same directory as this script
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.db')

# Disables SQLAlchemy event system, which can help improve performance
SQLALCHEMY_TRACK_MODIFICATIONS = False

