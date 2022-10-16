from flask import Blueprint, request, session
import json
from ..app import mysql
from ..app import auto

# create blue print to group routes
data_routes = Blueprint(
    'data_routes', __name__, template_folder = 'templates')


# route for getting list of visitors for hospitals
@data_routes.route('/getusers', methods = ['POST'])
@auto.doc()
def get_users():
    if "hospital" not in session:
        return "Unauthorized", 401

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # fetch selected properties
    query = ""
    if not name and (email or phone):
        query = f"""SELECT Visitor_name, Email, Phone_Number, Infected, Device_Id FROM Visitor
                    WHERE Email = '{email}' OR Phone_Number = '{phone}'"""
    else:
        query = f"""SELECT Visitor_name, Email, Phone_Number, Infected, Device_Id FROM Visitor
                    WHERE Visitor_name LIKE '%{name}%' OR Email = '{email}' OR Phone_Number = '{phone}'"""

    cur = mysql.connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    # convert result from python object to json to send
    resultJson = json.dumps(result)

    return resultJson


# route for updating the infection status of a visitor by hospital
@data_routes.route('/updateinfection', methods = ['POST'])
@auto.doc()
def update_visitor_infection():
    if "hospital" not in session:  # if not logged in as hospital
        return "Unauthorized", 401

    device_id = request.form['device_id']

    query = f"UPDATE Visitor SET Infected = !Infected WHERE Device_id = '{device_id}'"
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()

    return "done"  # return confirmation


# route for getting visitors by agent
@data_routes.route('/getusersagent', methods = ['POST'])
@auto.doc()
def getusers_agent():
    if "agent" not in session:  # if not logged in as agent
        return "Unauthorized", 401

    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']

    # fetch selected properties
    query = ""
    if not name and (email or phone):
        query = f"""SELECT * FROM Visitor WHERE Email = '{email}' OR Phone_Number = '{phone}'"""
    else:
        query = f"""SELECT * FROM Visitor
                    WHERE Visitor_name LIKE '%{name}%' OR Email = '{email}' OR Phone_Number = '{phone}'"""
    
    cur = mysql.connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    resultJson = json.dumps(result)

    return resultJson


# route for getting places for agent
@data_routes.route('/getplacesagent', methods = ['POST'])
@auto.doc()
def getplaces_agent():
    if "agent" not in session:
        return "Unauthorized", 401

    name = request.form['name']

    query = f"SELECT * FROM Place WHERE Place_name LIKE '%{name}%'"
    cur = mysql.connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    resultJson = json.dumps(result)

    return resultJson


# route for getting list of hospitals by agent
@data_routes.route('/gethospitals', methods = ['POST'])
@auto.doc()
def get_hospitals():
    if "agent" not in session:
        return "Unauthorized", 401

    query = f"SELECT * FROM Hospital"
    cur = mysql.connection.cursor()
    cur.execute(query)
    result = cur.fetchall()
    resultJson = json.dumps(result)

    return resultJson