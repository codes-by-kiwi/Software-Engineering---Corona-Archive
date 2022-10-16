from flask import Flask, render_template, url_for
#from flask_sqlalchemy import SQLAlchemy#

app= Flask(__name__)

# telling where our sqlite database called test is located

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# initilaizing databases

#db= SQLAlchemy(app)#





@app.route('/')

def index():
    return render_template("homepage.html")



@app.route('/registration')
def register():
    return render_template("registration.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/upload')
def upload():
    return render_template("upload.html")

@app.route('/scan')
def scan():
    return render_template("scan.html")


if __name__ =="__main__":
    app.run(debug=True)
