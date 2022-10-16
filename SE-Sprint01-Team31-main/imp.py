from flask import Flask, render_template, url_for, request, redirect
from datetime import datetime
import sqlite3
from sqlite3 import Error

app = Flask(__name__)

def create_connection(db_file):
    connection = None;
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)
        
    return conn
    
create_connection("coronaarchive.db")

def create_table(conn, users):
    sql = """ INSERT INTO users(user_firstname, user_phoneno, user_emailadd, user_address, user_lastname) VALUES(?,?,?,?,?) """
    c = conn.cursor()
    c.execute(sql, users)
    return cur.lastrowid
    
def main():
    database ="coronaarchive.db"
    
    sql_create_users_table = """ CREATE TABLE IF NOT EXISTS users (
                                    user_id integer PRIMARY KEY,
                                    user_firstname text NOT NULL,
                                    user_phoneno text NOT NULL UNIQUE,
                                    user_emailadd text NOT NULL UNIQUE,
                                    user_address text,
                                    user_lastname text NOT NULL
);"""
    conn = create_connection(database)

    if conn is not None:
        create_table(conn, sql_create_users_table)
    else:
        print("Error! cannot create the database connection.")
        
    @app.route('/')
    
    
    def index():
        return render_template("homepage.html")

    @app.route('/registration_form', methods=['POST'])
    def my_form():
    
        if request.method == 'POST':
            c = conn.cursor()
            user_firstname= request.form.get('First-Name')
            user_phoneno= request.form.get('Phone-Number')
            user_emailadd= request.form.get('Email-Address')
            user_address = request.form.get('Home-Address')
            user_lastname = request.form.get('Last-Name')

            try:
                sql = ("INSERT INTO databasename.tablename (columnName,columnName,columnName,columnName, columnName Ci) VALUES (%s, %s, %s, %s, %s)")
                c.execute(sql,(user_firstname, user_phoneno, user_emailadd,user_address, user_lastname))
                conn.commit() 
            #or "conn.commit()" (one of the two)
                return redirect('/')
            except:
                return 'Er ging iets fout met het opslaan van uw gegevens'
            finally:
                conn.close()

# This is where I run the app 
if __name__ == '__main__':
    app.run(debug=True)
    
    

