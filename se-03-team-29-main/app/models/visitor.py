from ..app import mysql
from ..utils.util import MissingInput
from datetime import datetime
from .place import Place
import json


import uuid


class Visitor:

    @classmethod
    def get_info(self, visitor_device_id):
        try:
            cursor = mysql.connection.cursor()
            get_visitor_info = f'SELECT * FROM Visitor WHERE device_id = "{visitor_device_id}"'

            cursor.execute(get_visitor_info)

            result = cursor.fetchall()

            if (len(result) == 0):
                raise Exception("Visitor does not exist")

            cursor.close()

            return result[0]

        except Exception:
            raise

    @classmethod
    def register(self, username, address, phone=None, email=None):
        device_id = uuid.uuid4()
        try:
            cursor = mysql.connection.cursor()
            if username == "" or address == "":
                raise Exception("Invalid Name or Address!")

            if phone == None:
                insertQuery = f'INSERT INTO Visitor(visitor_name, address, email, device_id) VALUES("{username}", "{address}", "{email}", "{device_id}")'
            elif email == None:
                insertQuery = f'INSERT INTO Visitor(visitor_name, address, phone_number, device_id) VALUES("{username}", "{address}", "{phone}", "{device_id}")'
            elif phone == None and email == None:
                raise Exception("Both Phone and Email can not be null!")
            else:
                insertQuery = f'INSERT INTO Visitor(visitor_name, address, email, phone_number, device_id) VALUES("{username}", "{address}","{email}", "{phone}", "{device_id}")'
                cursor.execute(insertQuery)
                mysql.connection.commit()

            cursor.close()

            return device_id
        except Exception:
            raise

    @classmethod
    def get_history(self, visitor_device_id):
        try:
            cursor = mysql.connection.cursor()
            searchQuery = f'SELECT * FROM VisitorsToPlaces WHERE device_id = "{visitor_device_id}" and exit_time IS NOT NULL'
            cursor.execute(searchQuery)

            results = cursor.fetchall()

            cursor.close()

            return results
        except Exception:
            raise

    @classmethod
    def checkin(self, visitor_device_id, qr_code):
        try:
            cursor = mysql.connection.cursor()
            entry_time = datetime.now()

            search_if_checkedin = f'SELECT * FROM VisitorsToPlaces WHERE device_id = "{visitor_device_id}" AND exit_time is NULL'
            cursor.execute(search_if_checkedin)

            result = cursor.fetchall()

            if len(result) != 0:
                raise Exception('Already checked into another place')

            insert_checkin = f'INSERT INTO VisitorsToPlaces(qr_code, device_id, entry_time) VALUES("{qr_code}", "{visitor_device_id}", "{entry_time}")'
            cursor.execute(insert_checkin)

            mysql.connection.commit()

            cursor.close()

            return entry_time

        except Exception:
            raise

    @classmethod
    def checkStatus(self, visitor_device_id):
        try:
            cursor = mysql.connection.cursor()

            search_if_checkedin = f'SELECT * FROM VisitorsToPlaces WHERE device_id = "{visitor_device_id}" AND exit_time is NULL'
            cursor.execute(search_if_checkedin)

            result = cursor.fetchall()

            if len(result) == 0:
                return None

            response = {}

            response['place'] = Place.getPlaceName(result[0][0])
            response['entry_time'] = str(result[0][2])

            return json.dumps(response)

        except Exception:
            raise

    @classmethod
    def checkOut(self, visitor_device_id):
        try:
            exit_time = datetime.now()
            cursor = mysql.connection.cursor()
            search_if_checkedin = f'SELECT * FROM VisitorsToPlaces WHERE device_id = "{visitor_device_id}" AND exit_time is NULL'
            cursor.execute(search_if_checkedin)
            result = cursor.fetchall()

            if len(result) == 0:
                raise Exception('Not logged into any place')

            update_exit_time = f'UPDATE VisitorsToPlaces SET exit_time="{exit_time}" WHERE device_id = "{visitor_device_id}"'
            cursor.execute(update_exit_time)

            mysql.connection.commit()
            cursor.close()

            return None

        except Exception:
            raise

    @classmethod
    def getAll(self):
        try:
            exit_time = datetime.now()
            cursor = mysql.connection.cursor()
            get_visitors = f'SELECT * FROM Visitor'

            cursor.execute(get_visitors)
            result = cursor.fetchall()

            cursor.close()

            return result

        except Exception:
            raise

    @classmethod
    def update_infection(self, visitor_device_id, infection_status):
        try:
            cursor = mysql.connection.cursor()
            update_status = f'UPDATE Visitor SET infected="{infection_status}" WHERE device_id = "{visitor_device_id}"'
            cursor.execute(update_status)

            mysql.connection.commit()
            cursor.close()
            return "Success"

        except Exception:
            raise

    @classmethod
    def search_visitor(self, visitor_name, visitor_device_id):
        try:
            cursor = mysql.connection.cursor()

            if visitor_device_id != "":
                get_visitors = f'SELECT * FROM Visitor WHERE Visitor_name LIKE CONCAT("{visitor_name}", "%") AND device_id = "{visitor_device_id}"'
            else:
                get_visitors = f'SELECT * FROM Visitor WHERE Visitor_name LIKE CONCAT("{visitor_name}", "%") OR device_id = "{visitor_device_id}"'

            cursor.execute(get_visitors)
            result = cursor.fetchall()
            cursor.close()
            return result
        except Exception:
            raise
