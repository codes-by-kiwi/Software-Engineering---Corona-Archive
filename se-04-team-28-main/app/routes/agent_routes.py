from flask import Blueprint, request, session,  render_template, redirect, url_for
import random
import string
from ..app import mysql
from ..app import auto

# create blueprint of routes to later add to main application
agent_routes = Blueprint(
    'agent_routes', __name__, template_folder = 'templates')


# password generation function
def generatePassword(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


# route for loggging in agent
@agent_routes.route('/login_agent', methods = ['GET', 'POST'])
@auto.doc()
def login_agent():
    if "agent" in session:  # if agent is already logged in
        return redirect('/agent_page')

    if request.method == "POST":
        agent = request.form["username"]
        password = request.form["password"]
        if not agent and not password:
            message = "Please enter Username and Password"
        else:
            cur = mysql.connection.cursor()
            query = f"SELECT * FROM Agent WHERE Username = '{agent}' AND Password = '{password}'"
            cur.execute(query)
            agent_account = cur.fetchone()
            
            if agent_account:  # if authentification is correct
                # creating a session for the agent
                session["agent"] = agent
                return redirect('/agent_page')
            else:
                message = "Wrong Username or Password"
        return render_template('login_agent.html', prompt = message), 400
    return render_template('login_agent.html')


# route for agent home page
@agent_routes.route('/agent_page', methods = ["GET"])
@auto.doc()
def agent_page():
    if "agent" not in session:  # if agent is not logged in
        return redirect('/login_agent')

    return render_template('agent_page.html')


# route for data base search page
@agent_routes.route('/search_database', methods = ["GET"])
@auto.doc()
def search_database():
    if "agent" not in session:  # if agent is not logged in
        return redirect('/login_agent')
    return render_template('search_database.html')


# route for registring a new hospital
@agent_routes.route('/register_hospital', methods = ['GET', 'POST'])
@auto.doc()
def register_hospital():
    # only the agent can register a hospital

    if "agent" not in session:
        return redirect('/login_agent')

    if request.method == "POST":
        username = request.form["username"]
        fields = [username]
        password = generatePassword(8)
        if username:
            cur = mysql.connection.cursor()
            query = f"SELECT 1 FROM Hospital WHERE Username = '{username}'"
            is_duplicate = cur.execute(query)
            if not is_duplicate:
                query = f"INSERT INTO Hospital(Username, Password) VALUES('{username}', '{password}')"
                cur.execute(query)
                mysql.connection.commit()
                message = f"Registered Username: {username} with Password: {password}"
                success = True
            else:
                message = "User already exists"
                success = False
        else:
            message = "Please enter Username"
            success = False
        return render_template("register_hospital.html", fields = fields,
                                prompt = message, success = success)
    return render_template("register_hospital.html", fields = [])


# route for agent logout
@agent_routes.route('/logout_agent')
@auto.doc()
def logout_agent():
    if "agent" in session:
        session.pop("agent", None)
        return redirect('/')
