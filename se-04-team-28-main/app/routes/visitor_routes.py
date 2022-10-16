from flask import Blueprint, request, session,  render_template, redirect, url_for
import re
import uuid
from datetime import datetime
from ..app import mysql
from ..app import auto


visitor_routes = Blueprint(
    'visitor_routes', __name__, template_folder='../templates')


# route for registering visitor
@visitor_routes.route('/register_visitor', methods = ['GET', 'POST'])
@auto.doc()
def register_visitor():

    if 'User_device_id' in session:
        return redirect('QR_code_scan')

    if request.method == 'POST':
        Vfullname = request.form.get('fullname')
        Vaddress = request.form.get('address')
        Vphonenumber = request.form.get('phonenumber')
        Vemail = request.form.get('email')
        fields = [Vfullname, Vaddress, Vphonenumber, Vemail]

        # input validation
        if not (Vphonenumber or Vemail):  # since we want phonenumber and/or email
            message = "Email or Phone number required"
        elif not Vfullname:  # checking if full name is entered
            message = "Name required"
        elif not Vaddress:  # checking if address is entered
            message = "Address required"
        else:
            Vdevice_id = uuid.uuid4()  # getting physical address
            session['User_device_id'] = Vdevice_id  # set session for visitor
            if not Vphonenumber:
                query = f"""INSERT INTO Visitor(Visitor_name, Address, Phone_Number, Email, Device_id)
                            VALUES('{Vfullname}', '{Vaddress}', NULL, '{Vemail}', '{Vdevice_id}')"""
                # message = "success"
            elif not Vemail:
                query = f"""INSERT INTO Visitor(Visitor_name, Address, Phone_Number, Email, Device_id)
                            VALUES('{Vfullname}', '{Vaddress}', '{Vphonenumber}', NULL, '{Vdevice_id}')"""
                # message = "success"
            else:
                query = f"""INSERT INTO Visitor(Visitor_name, Address, Phone_Number, Email, Device_id)
                            VALUES('{Vfullname}', '{Vaddress}', '{Vphonenumber}', '{Vemail}', '{Vdevice_id}')"""
                # message = "success"

            cur = mysql.connection.cursor()
            cur.execute(query)
            mysql.connection.commit()
            # message = "success"
            return redirect('/QR_code_scan')
        return render_template('register_visitor.html', fields = fields, prompt = message), 400
    return render_template('register_visitor.html', fields = [])


# route for getting home page (qr scanning page) of visitor
@visitor_routes.route('/QR_code_scan')
@auto.doc()
def qr_code_scan():
    if 'User_device_id' not in session:
        return redirect('register_visitor')
    return render_template('qr_code_scan.html')


# route for checking in at a place by visitor
@visitor_routes.route('/place/<id>')
@auto.doc()
def sign_in(id):
    if 'User_device_id' not in session:
        return redirect('/register_visitor')

    qr = id
    time = datetime.now()
    device_id = session['User_device_id']

    # get place name from QRcode
    cur = mysql.connection.cursor()
    name_query = f"SELECT Place_Name From Place WHERE QRcode='{qr}'"
    cur.execute(name_query)
    name_result = cur.fetchall()

    if len(name_result) != 0:
        print(name_result)
        place = name_result[0][0]
    else:
        return redirect('/')

    # check if visitor is already checked in at the place
    query = f"SELECT * FROM VisitorToPlace WHERE device_id='{device_id}' AND exit_time IS NULL"
    cur.execute(query)
    result = cur.fetchall()

    # if the visitor is already checked in, redirect them to that place's page
    if len(result) != 0 and id != result[0][0]:
        return redirect('/place/' + result[0][0])

    # if the user is not checked in at any place, create new entry
    if len(result) == 0:
        query = f"""INSERT INTO VisitorToPlace(QRcode, device_id, entry_time)
                    VALUES ('{qr}', '{device_id}','{time}')"""
        cur.execute(query)
        mysql.connection.commit()

        cur.close()
        return render_template('checked_in_place.html', placename = place, sign_in_time = time)
    else:
        # if the user has already checked in at the same place, get the entry time at that place
        command = f"""SELECT * FROM VisitorToPlace
                    WHERE QRcode='{qr}' AND device_id='{device_id}' AND exit_time IS NULL"""
        cur.execute(command)
        time = cur.fetchall()[0][2]
        cur.close()

        return render_template('checked_in_place.html', placename = place, sign_in_time = time)


# route for visitor to checkout of a place they are already logged in at
@visitor_routes.route('/signout', methods = ['POST'])
@auto.doc()
def signOut():

    # if user is not already logged in
    if 'User_device_id' not in session:
        return redirect('/')

    # obtain time and qr
    time = datetime.now()
    qr = request.form['qrcode']
    device_id = session['User_device_id']

    # query for updating exit time of record identified by qr, devce and entry time
    query = f"""UPDATE VisitorToPlace SET exit_time='{time}'
                WHERE QRcode='{qr}' AND device_id='{device_id}' AND exit_time is NULL"""
    cur = mysql.connection.cursor()
    cur.execute(query)
    mysql.connection.commit()

    return "Saved"  # return confirmation of signing out


# route for logging out visitor
@visitor_routes.route('/logout_visitor')
@auto.doc()
def logout_visitor():
    if "User_device_id" in session:
        session.pop("User_device_id", None)
        return redirect('/')