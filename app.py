from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from extensions import db
from models.models import User

from routes.auth_routes import auth_bp
from routes.main_routes import main_bp
from routes.quiz_routes import quiz_bp

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///coursehub.db'

db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = 'auth_routes.login'

@app.route('/')
def home():
    return '<h1>Welcome to CourseHub 🎓</h1><p><a href="/dashboard">Go to Dashboard</a></p>'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(auth_bp)
app.register_blueprint(main_bp)
app.register_blueprint(quiz_bp)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)