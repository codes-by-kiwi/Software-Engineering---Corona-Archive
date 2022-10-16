from flask import Blueprint, request, session, render_template
from ..app import app
from .agent_routes import agent_routes
from .hospital_routes import hospital_routes
from .place_routes import place_routes
from .visitor_routes import visitor_routes


def configure_routes(app):
    app.register_blueprint(agent_routes)
    app.register_blueprint(hospital_routes)
    app.register_blueprint(place_routes)
    app.register_blueprint(visitor_routes)

    @app.route("/", methods=["GET"])
    def homepage():
        visitor = session.get('visitor_device_id')
        place = session.get('place_device_id')
        agent = session.get('agent')
        hospital = session.get('hospital')
        return render_template("landingpage.html", visitor=visitor, place=place, agent=agent, hospital=hospital)
