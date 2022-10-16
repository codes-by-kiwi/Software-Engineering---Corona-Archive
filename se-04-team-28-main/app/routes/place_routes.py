from flask import Blueprint, request, session,  render_template, redirect, url_for
import uuid
import qrcode
import io
import base64
from ..app import mysql
from ..app import auto


place_routes = Blueprint(
    'place_routes', __name__, template_folder = 'templates')


def generate_QRcode(code):  # takes an input string and returns an encoded image
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill = 'black', back_color = 'white')
    data = io.BytesIO()
    img.save(data, "JPEG")
    encoded_image = base64.b64encode(data.getvalue())

    return encoded_image


# route for registering place
@place_routes.route('/register_place', methods = ['GET', 'POST'])
@auto.doc()
def register_place():

    if 'Place_device_id' in session:
        cur = mysql.connection.cursor()
        query = f"SELECT * from Place WHERE QRcode='{session['Place_device_id']}'"
        cur.execute(query)
        place_result = cur.fetchone()

        return render_template('/place_dashboard.html',
            info = (place_result[1], place_result[2], place_result[3]),
            encoded_image = generate_QRcode(session['Place_device_id']).decode('utf-8'))

    if request.method == 'POST':
        Vplacename = request.form.get('placename')
        Vaddress = request.form.get('address')
        if not Vplacename:
            message = "Missing place name"
        elif not Vaddress:
            message = "Missing place address"
        else:
            VQRcode = uuid.uuid4()  # creating the qrcode
            session['Place_device_id'] = VQRcode
            cur = mysql.connection.cursor()
            query = f"""INSERT INTO Place(Place_name, Address, QRcode)
                        VALUES('{Vplacename}', '{Vaddress}', '{VQRcode}')"""
            cur.execute(query)
            mysql.connection.commit()

            return render_template('place_dashboard.html',
                info = (Vplacename, Vaddress, VQRcode),
                encoded_image = generate_QRcode(VQRcode).decode('utf-8'))
        return render_template('register_place.html', prompt = message), 400
    return render_template('register_place.html')


# route for logging out place
@place_routes.route('/logout_place')
@auto.doc()
def logout_place():
    if "Place_device_id" in session:
        session.pop("Place_device_id", None)
        return redirect('/')