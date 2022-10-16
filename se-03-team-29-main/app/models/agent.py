from ..app import mysql


class Agent:
    @classmethod
    def login(self, username, password):
        try:
            cursor = mysql.connection.cursor()
            if username == None and password == None:
                raise Exception("Both username and password are required")

            findAgentQuery = f'SELECT * FROM Agent WHERE username="{username}"'
            cursor.execute(findAgentQuery)
            result = cursor.fetchall()

            if len(result) == 0:
                raise Exception("No agent by that username exists")

            if result[0][2] != password:
                raise Exception("Incorrect password")

            cursor.close()

            return username

        except Exception:
            raise  # if any error is found just raise it to the caller
