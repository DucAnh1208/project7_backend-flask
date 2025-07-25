from app.routes.auth import auth_bp
from app.routes.user import user_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(user_bp)