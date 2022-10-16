from flask import Blueprint, request, session, render_template, redirect
from ..models.visitor import Visitor
from ..models.place import Place
import qrcode
import io
import base64

place_routes = Blueprint(
    'place_routes', __name__, template_folder='templates')


def generate_QRcode(code):  # takes an input string and returns an encoded image
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5)
    qr.add_data(code)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    data = io.BytesIO()
    img.save(data, "JPEG")
    encoded_image = base64.b64encode(data.getvalue())

    return encoded_image


@place_routes.route("/place_signup", methods=["POST", "GET"])
def sign_up_place():
    if 'place_device_id' in session:
        return "None"

    if request.method == "GET":
        return "None", 405

    try:

        place_name = request.form["place_name"]
        address = request.form["address"]

        result = Place.register(place_name, address)
        session['place_device_id'] = result
        return redirect('/place_home')
    except Exception as err:
        print(err)
        return "None", 500


@place_routes.route('/place_home')
def place_home():
    if 'place_device_id' not in session:
        return redirect('/'), 401

    return render_template('place_home.html', encoded_image=generate_QRcode(session['place_device_id']).decode('utf-8'))


@place_routes.route('/place_logout')
def place_logout():
    if 'place_device_id' not in session:
        return redirect('/')
    session.pop('place_device_id', None)
    return redirect('/')
