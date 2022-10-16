from app.app import app
from app.routes.configure_routes import configure_routes

configure_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
