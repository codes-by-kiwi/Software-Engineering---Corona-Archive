from flask_mysqldb import MySQL
from urllib.parse import uses_relative
from click import prompt
from flask import Flask, redirect, render_template, request, url_for, Response, session
import yaml
from flask_selfdoc import Autodoc

# create the flask app
app = Flask(__name__)
auto = Autodoc(app)

# we want to encrypt the session data, this is done via the secret key, you can change it
app.secret_key = "aljdf5651%&/%DFS165$&&$&$"

# configuring the database
db = yaml.safe_load(open('./config/db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']
mysql = MySQL(app)

# importing all the created blueprints
from .routes.data_routes import data_routes
from .routes.hospital_routes import hospital_routes
from .routes.visitor_routes import visitor_routes
from .routes.agent_routes import agent_routes
from .routes.place_routes import place_routes

# register all the other routes from their blueprints
app.register_blueprint(data_routes)
app.register_blueprint(hospital_routes)
app.register_blueprint(agent_routes)
app.register_blueprint(visitor_routes)
app.register_blueprint(place_routes)


# create the home routes
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
	return render_template('login.html')

# create the about route
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/feedback')
def feedback():
	return render_template('feedback.html')

# Access to documentation with /docs after the link
@app.route('/docs')
def documentation():
    return auto.html(title='Corona Archive documentation')
