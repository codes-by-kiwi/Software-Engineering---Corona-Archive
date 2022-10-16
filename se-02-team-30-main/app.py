import pwd
from flask import Flask, render_template, redirect, request, url_for, flash, send_from_directory, abort, send_file
import sqlite3
from flask_debugtoolbar import DebugToolbarExtension
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

app.config['SECRET_KEY'] = 'team30'


DATABASE = './database/database.db'

# toolbar = DebugToolbarExtension(app)

if __name__ == "__main__":
    app.run()

app.debug = True
# making connection with database.


def get_db_connection():
    conn = sqlite3.connect('./database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

# ==========================Landing page=============================
# app.route is a decorator 
# / means root
# when we go to the root page the index function will run 
# so when you go to http://127.0.0.1:5000/ the result of index() should show
# every time you refresh the page it shows as a seperate line on the terminal for e.g:
# 127.0.0.1 - - [26/Mar/2022 15:02:05] "GET /option HTTP/1.1" 200 - 
# the above line means: 
# ipaddress - - [date accessed time accessed] "type of request method"

@app.route('/')
def index():
    return render_template('landing.html')

#when you put a random parameter inside result, you will get an internal server error
#when you run http://127.0.0.1:5000/moreinfo then the result() function should run
@app.route('/moreinfo')
def result():
    return render_template("moreinfo.html")

@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/lading')
def landing():
    return render_template('landing.html')


@app.route('/option')
def registerOption():
    return render_template('option.html')


# the route for Registration of visitor
@app.route('/visitorRegister', methods=('GET', 'POST'))
def visitorRegister():
    if request.method == 'POST':
        visitor_name = request.form['visitor_name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        email = request.form['email']
        device_ID = request.form['device_ID']
        infected = request.form['infected']

        if not visitor_name:
            flash('Name is required')
        elif not address:
            flash('Address is required')
        elif not phone_number:
            flash('phone_number is required')
        elif not email:
            flash('email is required')
        elif not device_ID:
            flash('device id is required')
        elif not infected:
            flash('infected is required')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Visitor (visitor_name, address, phone_number, email, device_ID, infected) VALUES(?, ?, ?, ?, ?, ?)',
                         (visitor_name, address, phone_number, email, device_ID, infected))
            conn.commit()
            conn.close()
            return redirect(url_for('visitorRegister'))

    return render_template('visitorRegister.html')

# The route for registration of place


@app.route('/placeRegister', methods=('GET', 'POST'))
def placeRegister():
    if request.method == 'POST':
        place_name = request.form['place_name']
        address = request.form['address']
        QRcode = request.form['QRcode']

        if not place_name:
            flash('Name is required')
        elif not address:
            flash('Address is required')
        elif not QRcode:
            flash('QRcode is required')

        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Places(place_name, address, QRcode) VALUES(?, ?, ?)',
                         (place_name, address, QRcode))
            conn.commit()
            conn.close()
            return redirect(url_for('placeRegister'))
    return render_template('placeRegister.html')

# the route for registration of agents


@ app.route('/agentRegister', methods=('GET', 'POST'))
def agentRegister():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash('Name is required')
        elif not password:
            flash('password is required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Agent(username, password) VALUES(?, ?)',
                         (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('agentRegister'))
    return render_template('agentRegister.html')

# the route for registration of hospitals


@ app.route('/hospitalRegister', methods=('GET', 'POST'))
def hospitalRegister():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username:
            flash('Name is required')
        elif not password:
            flash('password is required')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO Hospital(username, password) VALUES(?, ?)',
                         (username, password))
            conn.commit()
            conn.close()
            return redirect(url_for('hospitalRegister'))
    return render_template('hospitalRegister.html')

#path where you want to save images, tells that gifs and such are not allowed as uploads
#to see the files make sure you upload your personal path !!!
app.config["STATIC_VACCUPLOADS"] = "/Users/Denisa/Desktop/uni/2nd year/Spring 2022/Software Engineering/assignment 3/se-02-team-30/static/vaccuploads"
app.config["ALLOWED_IMAGE_EXTENSIONS"] = ["PNG","JPG","JPEG", "PDF"]

@app.route("/uploadImage", methods = ["GET", "POST"])
def uploadImage():

    if request.method == "POST":

        if request.files:

            image = request.files["image"]

            if image.filename == "":
                print("Image must have a filename")
                return redirect(request.url)

            image.save(os.path.join(app.config["STATIC_VACCUPLOADS"], image.filename))

            print("Image saved")

            return redirect(request.url)

    return render_template("uploadImage.html")

# the route for the QR code generator page
@ app.route('/QRcodegenerator')
def QRcodegenerator():
    return render_template('QRcodegenerator.html')

# allows client to download something
@ app.route("/get-Image/<img_name>", methods=['GET', 'POST'])
def get_Image(img_name):
    img = os.path.join(app.root_path,"/Users/Denisa/Desktop/uni/2nd year/Spring 2022/Software Engineering/assignment 3/se-02-team-30/static/client/img")
    return send_from_directory(directory=img,path=img_name, as_attachment=True)
