from flask import Flask
from app.routes import register_routes


def create_app():
    app = Flask(__name__)

    # đăng ký các routes (auth và user)
    register_routes(app)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
