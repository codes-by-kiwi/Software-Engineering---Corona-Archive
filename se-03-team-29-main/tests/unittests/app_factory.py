
from app.app import app
from app.routes.configure_routes import configure_routes


def build_app():
    configure_routes(app)

    return app
