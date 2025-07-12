import os

SECRET_KEY = os.environ.get("SECRET_KEY", "mysecretkey")
SQLALCHEMY_DATABASE_URI = 'sqlite:///database.db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY", "jwt-secret-key")
