from flask import Flask
from backend.auth import auth_bp
from backend.models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


app.register_blueprint(auth_bp)


@app.route('/')
def index():
    return 'Welcome to SmartHealth AI!'

if __name__ == '__main__':
    app.run(debug=True)
