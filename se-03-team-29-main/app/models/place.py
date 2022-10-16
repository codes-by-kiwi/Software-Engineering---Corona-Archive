from ..app import mysql
import uuid


class Place:
    @classmethod
    def register(self, place_name, address):
        qr_code = uuid.uuid4()

        try:
            cursor = mysql.connection.cursor()

            if place_name == "" or address == "":
                raise Exception("Both place name and address can not be null")

            if place_name == None or address == None:
                raise Exception("Both place name and address can not be null")

            insertQuery = f'INSERT INTO Place(place_name, address, qr_code) VALUES("{place_name}", "{address}","{qr_code}")'
            cursor.execute(insertQuery)
            mysql.connection.commit()

            cursor.close()

            return qr_code

        except Exception:
            raise

    @classmethod
    def getPlaceName(self, qr_code):
        try:
            cursor = mysql.connection.cursor()

            place_query = f'SELECT * FROM Place WHERE qr_code = "{qr_code}"'
            cursor.execute(place_query)

            result = cursor.fetchall()

            if len(result) == 0:
                raise Exception("No place by that qr")

            return result[0][1]

        except Exception:
            raise

    @classmethod
    def getAll(self):
        try:
            exit_time = datetime.now()
            cursor = mysql.connection.cursor()
            get_visitors = f'SELECT * FROM Place'

            cursor.execute(get_visitors)
            result = cursor.fetchall()

            cursor.close()

            return result

        except Exception:
            raise

    @classmethod
    def search_place(self, place_name):
        try:
            cursor = mysql.connection.cursor()
            get_visitors = f'SELECT * FROM Place WHERE place_name LIKE CONCAT("{place_name}", "%")'

            cursor.execute(get_visitors)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception:
            raise

    @classmethod
    def get_visitors(self, place_id):
        try:
            cursor = mysql.connection.cursor()
            get_visitors = f'select Visitor.visitor_name, Visitor.device_id, VisitorsToPlaces.entry_time, VisitorsToPlaces.exit_time from Visitor, VisitorsToPlaces where VisitorsToPlaces.device_id = Visitor.device_id AND VisitorsToPlaces.qr_code = "{place_id}"'
            cursor.execute(get_visitors)
            result = cursor.fetchall()
            cursor.close()
            return result

        except Exception:
            raise
