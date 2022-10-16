from flask import Blueprint, request, session, render_template, redirect
from ..models.hospital import Hospital
from ..models.visitor import Visitor
import json

hospital_routes = Blueprint(
    'hospital_routes', __name__, template_folder='templates')


# login page for the hospital
@hospital_routes.route("/hospital_login", methods=["POST", "GET"])
def hospital_login():
    if 'hospital' in session:
        return "None"

    if request.method == "GET":
        return "None", 405

    try:
        username = request.form["username"]
        password = request.form["password"]
        result = Hospital.login(username, password)
        session['hospital'] = result
        return "Success"
    except Exception as err:
        print(err)
        return "None"


@hospital_routes.route("/hospital_home")
def hospital_home():
    if 'hospital' not in session:
        return redirect('/')

    return render_template("hospital_home.html")


@hospital_routes.route("/hospital_logout")
def logout_hospital():
    if 'hospital' not in session:
        return redirect('/')

    session.pop('hospital', None)
    return redirect('/')


@hospital_routes.route("/hospital_visitor_lookup", methods=["POST", "GET"])
def hospital_visitor_lookup():
    if 'hospital' not in session:
        return redirect('/')

    response = []

    if request.method == "POST":
        visitor_name = request.form['visitor_name']
        visitor_device_id = request.form['device_id']

        try:
            result = Visitor.search_visitor(visitor_name, visitor_device_id)

            for record in result:
                response.append({
                    'visitor_name': record[1],
                    'device_id': record[5],
                    'infected': record[6]
                })

            return json.dumps(response)

        except Exception as err:
            print(err)
            return response

    try:
        result = Visitor.getAll()

        for record in result:
            response.append({
                'visitor_name': record[1],
                'device_id': record[5],
                'infected': record[6]
            })

        return json.dumps(response)

    except Exception:
        return json.dumps(response)


@hospital_routes.route("/hospital_visitor_update_infection", methods=["POST", "GET"])
def hospital_visitor_update_infection():
    if 'hospital' not in session:
        print("not in session")
        return "None"

    try:
        result = Visitor.update_infection(
            request.form['device_id'], request.form['infection'])

        return result

    except Exception as err:
        print(err)
        return "None"
