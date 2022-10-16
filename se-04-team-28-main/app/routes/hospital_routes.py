from flask import Blueprint, request, session,  render_template, redirect, url_for
from ..app import mysql
from ..app import auto


hospital_routes = Blueprint(
    'hospital_routes', __name__, template_folder = 'templates')


# route for logging in hospital
@hospital_routes.route('/login_hospital', methods = ['GET', 'POST'])
@auto.doc()
def login_hospital():
    if "hospital" in session:  # if not logged in as hospital
        return redirect('/hospital_dashboard')

    if request.method == "POST":
        hospital = request.form["username"]
        password = request.form["password"]
        if not hospital and not password:
            message = "Please enter Username and Password"
        else:
            cur = mysql.connection.cursor()
            query = f"""SELECT * FROM Hospital
                        WHERE Username = '{hospital}' AND Password = '{password}'"""
            cur.execute(query)
            hospital_account = cur.fetchone()

            if hospital_account:  # if authentification is correct
                # creating a session for the hospital
                session["hospital"] = hospital
                return redirect('/hospital_dashboard')
            else:
                message = "Wrong Username or Password"
        return render_template('login_hospital.html', prompt = message), 400
    return render_template('login_hospital.html')


# route for delivering hospital dashboard
@hospital_routes.route('/hospital_dashboard', methods = ['GET', 'POST'])
@auto.doc()
def hospital_dashboard():
    if "hospital" not in session:
        return redirect('/login_hospital')

    return render_template('hospital_dashboard.html')


# route for hospital logout
@hospital_routes.route('/logout_hospital')
@auto.doc()
def logout_hospital():
    if "hospital" in session:
        session.pop("hospital", None)
        return redirect('/')
