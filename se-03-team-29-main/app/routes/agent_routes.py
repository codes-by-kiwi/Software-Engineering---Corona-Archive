from flask import Blueprint, request, session, render_template, redirect
from ..models.agent import Agent
from ..models.visitor import Visitor
from ..models.place import Place
from ..models.hospital import Hospital
import json

agent_routes = Blueprint(
    'agent_routes', __name__, template_folder='templates')


@agent_routes.route("/agent_login", methods=["POST", "GET"])
def agent_login():
    if 'agent' in session:
        return redirect('/agent_home')

    if request.method == 'GET':
        return "None", 405

    try:
        username = request.form["username"]
        password = request.form["password"]
        result = Agent.login(username, password)
        session['agent'] = result
        return "Success"
    except Exception as err:
        print(err)
        return "None"


@agent_routes.route('/agent_home')
def agent_home():
    if 'agent' not in session:
        return redirect('/')
    return render_template('agent_home.html')


@agent_routes.route('/agent_logout')
def agent_logout():
    if 'agent' not in session:
        return redirect('/')
    session.pop('agent', None)
    return redirect('/')


@agent_routes.route('/visitor_fetch')
def visitor_fetch():
    if 'agent' not in session:
        return redirect('/agent_login')

    result = Visitor.getAll()

    response = []

    for record in result:
        response.append({
            'visitor_name': record[1],
            'address': record[2],
            'email': record[3],
            'phone_number': record[4],
            'device_id': record[5],
            'infected': record[6]
        })

    return json.dumps(response)


@agent_routes.route("/agent_visitor_lookup", methods=["POST", "GET"])
def hospital_visitor_lookup():
    if 'agent' not in session:
        return redirect('/agent_login')

    response = []

    if request.method == "POST":
        visitor_name = request.form['visitor_name']
        visitor_device_id = request.form['device_id']

        try:
            result = Visitor.search_visitor(visitor_name, visitor_device_id)

            for record in result:
                response.append({
                    'visitor_name': record[1],
                    'address': record[2],
                    'email': record[3],
                    'phone_number': record[4],
                    'device_id': record[5],
                    'infected': record[6]
                })

            return json.dumps(response)

        except Exception as err:
            print(err)
            return json.dumps(response)

    try:
        result = Visitor.getAll()

        for record in result:
            response.append({
                'visitor_name': record[1],
                'address': record[2],
                'email': record[3],
                'phone_number': record[4],
                'device_id': record[5],
                'infected': record[6]
            })

        return json.dumps(response)

    except Exception:
        return json.dumps(response)


@agent_routes.route("/agent_place_lookup", methods=["POST", "GET"])
def agent_place_fetch():
    if 'agent' not in session:
        return json.dumps([])

    response = []

    if request.method == "POST":
        place_name = request.form['place_name']

        try:
            result = Place.search_place(place_name)

            for record in result:
                response.append({
                    'place_name': record[1],
                    'address': record[2],
                    'place_id': record[3]
                })

            return json.dumps(response)

        except Exception as err:
            print(err)
            return json.dumps(response)

    try:
        result = Place.getAll()

        for record in result:
            response.append({
                'visitor_name': record[1],
                'address': record[2],
            })

        return json.dumps(response)

    except Exception:
        return json.dumps(response)


@agent_routes.route('/agent_visitor_history', methods=["POST"])
def agent_visitor_history():
    if 'agent' not in session:
        return json.dumps([])

    response = []

    if request.method == "POST":
        visitor_device_id = request.form['device_id']

        try:
            result = Visitor.get_history(visitor_device_id)

            for record in result:
                response.append({
                    'place_name': Place.getPlaceName(record[0]),
                    'entry_time': str(record[2]),
                    'exit_time': str(record[3])
                })

            return json.dumps(response)

        except Exception as err:
            print(err)
            return json.dumps(response)

    try:
        result = Visitor.getAll()

        for record in result:
            response.append({
                'visitor_name': record[1],
                'address': record[2],
                'email': record[3],
                'phone_number': record[4],
                'device_id': record[5],
                'infected': record[6]
            })

        return json.dumps(response)

    except Exception:
        return json.dumps(response)


@agent_routes.route('/agent_place_history', methods=["POST"])
def agent_place_history():
    if 'agent' not in session:
        return json.dumps([])

    response = []

    place_id = request.form['place_id']

    try:
        result = Place.get_visitors(place_id)

        for record in result:
            response.append({
                'visitor_name': record[0],
                'visitor_id': record[1],
                'entry_time': str(record[2]),
                'exit_time': str(record[3])
            })

        return json.dumps(response)
    except Exception as err:
        print(err)
        return json.dumps(response)


@agent_routes.route("/agent_register_hospital", methods=["POST"])
def register_hospital():
    if "agent" not in session:
        return "None"

    try:
        hospital_username = request.form["hospital_username"]

        password = Hospital.register(hospital_username)

        return password

    except Exception as err:
        print(err)
        return "None"
