from flask import Flask
from .routes.auth import auth_bp  # import đúng tên file auth.py
from .routes.user import user_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp)  # đăng ký route login
    app.register_blueprint(user_bp)
    return app
