from ..app import mysql
import random
import string


class Hospital:
    # password generation function
    def generate_password(length):
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))

        return result_str

    @classmethod
    def login(self, username, password):
        try:
            cursor = mysql.connection.cursor()
            if username == None and password == None:
                raise Exception("Both username and password are required")

            findAgentQuery = f'SELECT * FROM Hospital WHERE username="{username}"'
            cursor.execute(findAgentQuery)
            result = cursor.fetchall()

            if len(result) == 0:
                raise Exception("No hospital by that username exists")

            if result[0][2] != password:
                raise Exception("Incorrect password")

            cursor.close()

            return username

        except Exception:
            raise

    @classmethod
    def register(self, hospital_username):
        try:
            cursor = mysql.connection.cursor()

            unique_username_check = f'SELECT * FROM Hospital WHERE username="{hospital_username}"'
            cursor.execute(unique_username_check)
            result = cursor.fetchall()

            if len(result) != 0:
                raise Exception("Username is already being used")

            password = Hospital.generate_password(8)

            insert_hospital = f'INSERT INTO Hospital(username, password) VALUES ("{hospital_username}", "{password}")'

            cursor.execute(insert_hospital)
            mysql.connection.commit()

            cursor.close()

            return password

        except Exception:
            raise
