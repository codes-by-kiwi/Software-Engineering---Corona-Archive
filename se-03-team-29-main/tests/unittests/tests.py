import unittest
from .app_factory import build_app
from flask import json

app = build_app()


class MainTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    # tests to check the single unprotected route is working
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


class HospitalTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_hospitalLoginInvalid(self):
        """
            Testing hospital login with invalid data (non exsistent username and password)
        """
        response = self.app.post('/hospital_login', data=dict(username="",
                                                              password=""), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'None', response.data)

    def test_hospitalLoginValid(self):
        """
            Testing hospital login with valid data (exisiting username and password)
        """
        response = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                              password="password"), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'Success', response.data)

    def test_hospitalHomePage(self):
        """
            Testing the rendering of hospital homepage after login and redirect
        """

        response = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                              password="password"), follow_redirects=True)
        # flask test unit should now have a valid agent cookie

        response2 = self.app.get('/hospital_home', follow_redirects=True)

        self.assertEqual(response2.status_code, 200)

    def test_hospitalVisitorLookupPage(self):
        """
            Testing the rendering of visitor lookup on hospital homepage with the required
            interface components
        """

        response = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                              password="password"), follow_redirects=True)

        response2 = self.app.get('/hospital_home', follow_redirects=True)

        self.assertIn(b'<table class="visitor_table">', response2.data)

    def test_hospitalVisitorSearchByNameValid(self):
        """
            Testing the hospital visitor search functionality by logging in
            as hospital then registering as a visitor then searching for that visitor
        """
        response = self.app.post('/visitor_signup', data=dict(username="newtestuser",
                                                              address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        response2 = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                               password="password"), follow_redirects=True)

        response3 = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="newtestuser", device_id=""), follow_redirects=True)

        self.assertTrue(len(json.loads(response3.data)) > 0)

    def test_hospitalVisitorSearchByNameInvalid(self):
        """
            Testing the hospital visitor name search with a wrong
            visitor name
        """

        response2 = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                               password="password"), follow_redirects=True)

        response3 = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="nonexistentuser", device_id=""), follow_redirects=True)

        self.assertTrue(len(json.loads(response3.data)) == 0)

    def test_hospitalVisitorSearchByIdValid(self):
        """
            Testing the hospital visitor search by id by first finding a valid id then searching using that id
            and making sure only one result is returned
        """
        response2 = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                               password="password"), follow_redirects=True)

        response3 = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="", device_id=""), follow_redirects=True)

        device_id = json.loads(response3.data)[0]["device_id"]

        response4 = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="", device_id=device_id), follow_redirects=True)

        self.assertTrue(len(json.loads(response4.data)) == 1)

    # tests to check the hospital visitor infection setting toggle

    def test_hospitalVisitorInfectionToggle(self):
        """
            Testing the hospital visitor infection toggle by first finding a valid visitor id and toggling
            that and checking whether the result is changed
        """

        hospital_login = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                                    password="password"), follow_redirects=True)

        visitor_fetch = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="", device_id=""), follow_redirects=True)

        device_id = json.loads(visitor_fetch.data)[0]["device_id"]
        infected = json.loads(visitor_fetch.data)[0]["infected"]

        response4 = self.app.post(
            '/hospital_visitor_update_infection', data=dict(device_id=device_id, infection=0 if infected == 1 else 1), follow_redirects=True)

        response5 = self.app.post(
            '/hospital_visitor_lookup', data=dict(visitor_name="", device_id=device_id), follow_redirects=True)

        self.assertFalse(infected == json.loads(response5.data)[0]["infected"])

    def test_hospitalLogout(self):
        """
            Testing the hospital visitor logout function by first logging in then logging out
            then trying to access a protected route
        """
        response = self.app.post('/hospital_login', data=dict(username="hospital1",
                                                              password="password"), follow_redirects=True)
        response2 = self.app.get('/hospital_logout', follow_redirects=True)

        response3 = self.app.get('/hospital_home', follow_redirects=True)

        self.assertIn(b' <form id="agent_hospital_form">', response3.data)


class VisitorTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_visitorRegistrationInvalid(self):
        """
            Testing registration with empty fields which is invalid
        """
        response = self.app.post('/visitor_signup', data=dict(username="",
                                                              address="", phone="", email=""), follow_redirects=True)
        self.assertEqual(response.status_code, 500)

    def test_visitorRegistrationValid(self):
        """
            Testing registration with full fields and checking if visitor home page is returned
        """
        response = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                              address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'<div class="visitor_info">', response.data)

    def test_visitorRegistrationForm(self):
        """
            Testing the existence of the required dom elements for visitor registration
        """

        response = self.app.get('/', follow_redirects=True)
        self.assertIn(
            b'<form id="visitor_form" style="display: none;" action="/visitor_signup" method="POST">', response.data)

    def test_visitorHomePage(self):
        """
            Testing the return value of visitor homepage for the required components
        """

        response = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                              address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)
        # valid visitor cookie should be set on the test object

        response2 = self.app.get('/visitor_home', follow_redirects=True)

        self.assertIn(
            b'<div class="checkin_history" id="history_table_container">', response.data)

    def test_visitorCheckinValid(self):
        """
            Testing to check if the login of visitor is valid by looking for a valid place id
            then passing that place id to the respective route
        """
        response = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                              address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        response2 = self.app.post('/agent_login', data=dict(username="agent1",
                                                            password="password"), follow_redirects=True)

        response3 = self.app.post(
            '/agent_place_lookup', data=dict(place_name=""), follow_redirects=True)

        place_id = json.loads(response3.data)[0]['place_id']

        response4 = self.app.post(
            '/agent_place_history', data=dict(place_id=place_id), follow_redirects=True)

        initial_count = len(json.loads(response4.data))

        response5 = self.app.get('/place/' + place_id, follow_redirects=True)

        response6 = self.app.post(
            '/agent_place_history', data=dict(place_id=place_id), follow_redirects=True)

        added_count = len(json.loads(response6.data))

        self.assertTrue(added_count == initial_count+1)

    def test_visitorCheckinInvalid(self):
        """
            Testing if a visitor already checked into one place can check into another place
            by checking into one place then attempting to check into a different place
        """

        visitor_signup = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                                    address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        agent_login = self.app.post('/agent_login', data=dict(username="agent1",
                                                              password="password"), follow_redirects=True)

        place1_signup = self.app.post('/place_signup', data=dict(place_name="testplace",
                                                                 address="testaddress"), follow_redirects=True)

        place1_logout = self.app.get('/place_logout', follow_redirects=True)

        place2_signup = self.app.post('/place_signup', data=dict(place_name="testplace",
                                                                 address="testaddress"), follow_redirects=True)

        place_ids_fetch = self.app.post(
            '/agent_place_lookup', data=dict(place_name=""), follow_redirects=True)

        place1_id = json.loads(place_ids_fetch.data)[0]['place_id']
        place2_id = json.loads(place_ids_fetch.data)[1]['place_id']

        checkin_place1 = self.app.get(
            '/place/' + place1_id, follow_redirects=True)
        # should work up until here

        checkin_place2 = self.app.get(
            '/place/' + place2_id, follow_redirects=True)

        self.assertEqual(checkin_place2.status_code, 500)

    def test_visitorHistoryFetching(self):
        """
            Testing the visitor history fetching route by signing up as a visitor
            and calling the route
        """

        visitor_signup = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                                    address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        visitor_history_fetching = self.app.get(
            '/visitor_history', follow_redirects=True)

        self.assertEqual(visitor_history_fetching.status_code, 200)

    # tests to check the delete account and logout funcitonality of visitor

    def test_visitorLogout(self):
        """
            Testing the visitory logout route by signing up as a user then logging out then
            attempting to access a protected visitor route
        """
        visitor_signup = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                                    address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        visitor_logout = self.app.get('/visitor_logout', follow_redirects=True)

        protected_route_access = self.app.get(
            '/visitor_home', follow_redirects=True)

        self.assertIn(b'<form id="visitor_form"', protected_route_access.data)


class PlaceTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_placeRegistrationInvalid(self):
        """
            Testing registration with empty fields which is invalid
        """

        response = self.app.post('/place_signup', data=dict(place_name="",
                                                            address=""), follow_redirects=True)
        self.assertEqual(response.status_code, 500)

    def test_placeRegistrationValid(self):
        """
            Testing registration with full fields and checking if place home page is returned
        """
        response = self.app.post('/place_signup', data=dict(place_name="testplace",
                                                            address="testaddress"), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'<img src="data:image/jpeg;base64', response.data)

    def test_placeRegistrationForm(self):
        """
            Testing the rendering of the place registration page
        """

        response = self.app.get('', follow_redirects=True)
        self.assertIn(
            b'<form id="place_form" ', response.data)

    def test_placeHomePage(self):
        """
            Testing the rendering of the place home page after registration
        """

        response = self.app.post('/place_signup', data=dict(place_name="testplace",
                                                            address="testaddress"), follow_redirects=True)

        response2 = self.app.get('/place_home', follow_redirects=True)

        self.assertIn(
            b'<img src="data:image/jpeg;base64', response.data)


class AgentTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_agentLoginInvalid(self):
        """
            Testing agent login with invalid data (non existent username and password)
        """
        response = self.app.post('/agent_login', data=dict(username="",
                                                           password=""), follow_redirects=True)

        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'None', response.data)

    def test_agentHomePage(self):
        """
            Testing the rendering of agent homepage after login and redirect
        """

        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)
        # flask test unit should now have a valid agent cookie

        response2 = self.app.get('/agent_home', follow_redirects=True)

        self.assertEqual(response2.status_code, 200)

    def test_agentVisitorLookupPage(self):
        """
            Testing the rendering of visitor lookup on agent homepage with the required
            interface components
        """
        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)
        # flask test unit should now have a valid agent cookie

        response2 = self.app.get('/agent_home', follow_redirects=True)

        self.assertIn(b'<table class="visitor_table">', response2.data)

    def test_agentPlaceLookupPage(self):
        """
            Testing the rendering of place lookup on agent homepage with the required
            interface components
        """

        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)

        response2 = self.app.get('/agent_home', follow_redirects=True)

        self.assertIn(b'<table class="visitor_table">', response2.data)

    def test_agentHospitalRegistrationPage(self):
        """
            Testing the rendering of place hospital registration components
        """
        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)

        response2 = self.app.get('/agent_home', follow_redirects=True)

        self.assertIn(b' <div id="hospital_registration_form"', response2.data)

    def test_agentVisitorFetchValid(self):
        """
            Testing the visitor searching of agent by logging in agent and
            registerting a visitor here then searching for that visitor
        """
        response = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                              address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        response2 = self.app.post('/agent_login', data=dict(username="agent1",
                                                            password="password"), follow_redirects=True)

        response3 = self.app.get('/visitor_fetch', follow_redirects=True)

        self.assertEqual(response3.status_code, 200)

    # tests to check agent place lookup

    def test_agentPlaceLookupValid(self):
        """
            Testing the place searching of place
        """

        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)

        response2 = self.app.post(
            '/agent_place_lookup', data=dict(place_name=""), follow_redirects=True)

        self.assertEqual(response2.status_code, 200)

    # tests to check agent lookup of infected visitor place history

    def test_agentInfectedVisitorPlaceHistory(self):
        """
            Testing the visitor history fetching functionality of agent
        """

        agent_login = self.app.post('/agent_login', data=dict(username="agent1",
                                                              password="password"), follow_redirects=True)

        visitor_signup = self.app.post('/visitor_signup', data=dict(username="testuser",
                                                                    address="testaddress", phone="+2510933432394", email="testemail@email.com"), follow_redirects=True)

        fetch_visitor = self.app.get('/visitor_fetch', follow_redirects=True)

        device_id = json.loads(fetch_visitor.data)[0]['device_id']

        check_history = self.app.post(
            '/agent_visitor_history', data=dict(device_id=device_id), follow_redirects=True)

        self.assertTrue(len(json.loads(check_history.data)) == 0)

    # tests to check the logout function of agent

    def test_agentLogout(self):
        """
            Testing the logout funcitonality of agent by logging in as agent,
            then logging out, then trying to access a protected route
        """

        response = self.app.post('/agent_login', data=dict(username="agent1",
                                                           password="password"), follow_redirects=True)

        response2 = self.app.get('/agent_logout', follow_redirects=True)

        response3 = self.app.get('/agent_home', follow_redirects=True)

        self.assertIn(
            b' <form id="agent_hospital_form">', response3.data)


if __name__ == "__main__":
    unittest.main()
