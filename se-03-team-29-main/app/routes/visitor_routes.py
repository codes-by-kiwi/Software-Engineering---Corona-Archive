
from flask import Blueprint, request, session, render_template, redirect
from ..models.visitor import Visitor
from ..models.visitor import Place
from ..utils.util import MissingInput
import json

visitor_routes = Blueprint(
    'visitor_routes', __name__, template_folder='templates')


@visitor_routes.route("/visitor_signup", methods=["POST", "GET"])
def visitor_signup():
    """ 
        non-ajax route
    """
    if 'visitor_device_id' in session:
        return "None"

    if request.method == 'GET':
        return "None", 405

    try:
        visitor_name = request.form["username"]
        address = request.form["address"]
        phone = request.form["phone"]
        email = request.form["email"]
        result = Visitor.register(visitor_name, address, phone, email)
        session['visitor_device_id'] = result

        return redirect('/visitor_home')

    except Exception as err:
        return "None", 500


@visitor_routes.route('/visitor_home')
def visitor_home():

    if 'visitor_device_id' not in session:
        return redirect('/')

    return render_template('visitor_home.html')


@visitor_routes.route('/visitor_scanin')
def visitor_scanin():
    if 'visitor_device_id' not in session:
        return redirect('/')
    return render_template('visitor_scanin.html')


# data routes (non rendering routes)

@visitor_routes.route('/place/<place_id>')
def visitor_place(place_id):
    if 'visitor_device_id' not in session:
        return "None", 401

    try:
        entry_time = Visitor.checkin(session['visitor_device_id'], place_id)

        return redirect('/visitor_home')

    except Exception as err:
        return redirect('/visitor_home'), 500


@visitor_routes.route('/visitor_history')
def visitor_history():
    if 'visitor_device_id' not in session:
        return "None", 401

    try:

        visitor = session['visitor_device_id']

        result = Visitor.get_history(visitor)

        response = []

        for record in result:
            response.append({
                'place_name': Place.getPlaceName(record[0]),
                'entry_time': str(record[2]),
                'exit_time': str(record[3])
            })

        return json.dumps(response)

    except Exception as err:
        print(err)
        return json.dumps([]), 500


@visitor_routes.route('/visitor_check')
def visitor_check():
    if 'visitor_device_id' not in session:
        return "None", 401

    try:

        visitor = session['visitor_device_id']

        result = Visitor.checkStatus(visitor)

        return str(result)

    except Exception as err:
        print(err)
        return "None", 500


@visitor_routes.route('/visitor_checkout')
def visitor_checkout():
    if 'visitor_device_id' not in session:
        return "None", 401

    try:
        visitor = session['visitor_device_id']

        Visitor.checkOut(visitor)

        return "None"

    except Exception as err:
        print(err)
        return "None", 500


@visitor_routes.route('/visitor_info', methods=["GET"])
def visitor_info():
    if 'visitor_device_id' not in session:
        return json.dumps({}), 401

    try:
        visitor_device_id = session['visitor_device_id']

        result = Visitor.get_info(visitor_device_id)
        response = {
            'visitor_name': result[1],
            'address': result[2],
            'email': result[3],
            'phone_number': result[4],
            'device_id': result[5],
            'infection_status': result[6]
        }

        return json.dumps(response)

    except Exception as err:
        print(err)
        return json.dumps({}), 500


@visitor_routes.route('/visitor_logout', methods=["GET"])
def visitor_logout():
    if 'visitor_device_id' not in session:
        return redirect('/'), 401

    try:
        session.pop('visitor_device_id', None)

        return redirect('/')

    except Exception as err:
        print(err)
        return redirect('/'), 500
