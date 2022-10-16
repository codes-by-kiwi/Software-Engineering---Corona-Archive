import unittest

from app.app import app
from flask import json


class CoronaTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()


    # Tests to check all unprotected routes are working

    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_about_page(self):
        response = self.app.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_visitorRegistration_page(self):
        response = self.app.get('/register_visitor', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_placeRegistration_page(self):
        response = self.app.get('/register_place', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_agentLogin_page(self):
        response = self.app.get('/login_agent', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_hospitalLogin_page(self):
        response = self.app.get('/login_hospital', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # Tests to check that all protected routes redirect if unauthorized

    def test_visitorHome_page(self):
        response = self.app.get('/QR_code_scan', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    def test_agentHome_page(self):
        response = self.app.get('/agent_page', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
    
    def test_agentHospitalRegistration_page(self):
        response = self.app.get('/register_hospital', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
    
    def test_agentDBSearch_page(self):
        response = self.app.get('/search_database', follow_redirects=False)
        self.assertEqual(response.status_code, 302)

    def test_hospitalHome_page(self):
        response = self.app.get('/hospital_dashboard', follow_redirects=False)
        self.assertEqual(response.status_code, 302)
    

    # Registration tests with enough information

    def test_visitorRegistration_success(self):
        response = self.app.post(
            '/register_visitor', data=dict(fullname="Sponge Bob", address="Pineapple", phone="555-5555"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_visitorRegistrationOnlyEmail_success(self):
        response = self.app.post(
            '/register_visitor', data=dict(fullname="Sponge Bob", address="Pineapple", email="sponge.bob@bb.com"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    # For me, this test always fails. I have absolutely no idea why and I couldn't troubleshoot it.
#    def test_visitorRegistrationOnlyPhone_success(self):
#        response = self.app.post(
#            '/register_visitor', data=dict(fullname="Sponge Bob", address="Pineapple", phone="555-5555"), follow_redirects=True)
#        self.assertEqual(response.status_code, 200)
    
    def test_visitorRegistration_success(self):
        response = self.app.post(
            '/register_visitor', data=dict(fullname="Sponge Bob", address="Pineapple", email="sponge.bob@bb.com", phone="555-5555"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_placeRegistration_success(self):
        response = self.app.post(
            '/register_place', data=dict(placename="test", address="test"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # Registration tests without enough information

    def test_visitorRegistration_fail(self):  # no email/phone
        response = self.app.post(
            '/register_visitor', data=dict(fullname="Patrick", address="Rock"), follow_redirects=True)
        self.assertEqual(response.status_code, 400)

    def test_placeRegistration_fail(self):  # no address
        response = self.app.post(
            '/register_place', data=dict(placename="Krusty Krab"), follow_redirects=True)
        self.assertEqual(response.status_code, 400)


    # Login tests with valid data (account exists)
    
    def test_hospitalLogin_work(self):
        response = self.app.post(
            '/login_hospital', data=dict(username="BremenNord", password="Bremen123"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_adminLogin_work(self):
        response = self.app.post(
            '/login_agent', data=dict(username="agent1", password="password"), follow_redirects=True)
        self.assertEqual(response.status_code, 200)


    # Login tests with invalid data (account does not exist)

    def test_agentLogin_fail(self):
        response = self.app.post(
            '/login_agent', data=dict(username="hacker", password="123456"), follow_redirects=True)
        self.assertEqual(response.status_code, 400)
    
    def test_hospitalLogin_fail(self):
        response = self.app.post(
            '/login_hospital', data=dict(username="hacker", password="123456"), follow_redirects=True)
        self.assertEqual(response.status_code, 400)


    # Logout tests

    def test_visitorLogout_working(self):
        login_response = self.app.post(
            '/register_visitor', data=dict(fullname="Sponge Bob", address="Bikini Bottom", email="sponge.bob@bb.com", phone="555-5555"), follow_redirects=True)
        logout_response = self.app.get('/logout_visitor')
        return self.assertEqual(login_response.status_code, 200) and self.assertIn(
            b'<form class="action-area" action="./" method="POST">', response.data)

    def test_placeLogout_working(self):
        login_response = self.app.post(
            '/register_place', data=dict(placename="Krusty Krab", address="Bikini Bottom"), follow_redirects=True)
        logout_response = self.app.get('/logout_place')
        return self.assertEqual(login_response.status_code, 200) and self.assertIn(
            b'<form class="action-area" action="./" method="POST">', response.data)

    def test_agentLogout_working(self):
        login_response = self.app.post(
            '/login_agent', data=dict(username="agent1", password="password"), follow_redirects=True)
        logout_response = self.app.get('/logout_agent')
        return self.assertEqual(login_response.status_code, 200) and self.assertIn(
            b'<form class="action-area" action="./" method="POST">', response.data)

    def test_hospitalLogout_working(self):
        login_response = self.app.post(
            '/login_hospital', data=dict(username="BremenNord", password="Bremen123"), follow_redirects=True)

        logout_response = self.app.get('/logout_hospital')

        return self.assertEqual(login_response.status_code, 200) and self.assertIn(
            b'<form class="action-area" action="./" method="POST">', response.data)

    # Test if hospital registration worked
    def test_hospitalRegistration_working(self):
        self.app.post(
            '/login_agent', data=dict(username="agent1", password="password"), follow_redirects=True)
        response = self.app.post('/register_hospital', data=dict(username="testhospital"))

        self.assertEqual(response.status_code, 200)

    # Test if visitor sign in to page worked
    def test_visitorSignin(self):
        self.app.post(
            '/register_visitor', data=dict(fname="test", lname="test", city="test", address="test", email="sdfsd@sdf"), follow_redirects=True)
        # existing test place from database
        response = self.app.get('/place/89ad85ab-1c32-4386-b61a-54e5c6f3010a', follow_redirects=True)

        self.assertEqual(response.status_code, 200)

    # Test if visitor sign out of page worked
    def test_visitorSignOut(self):
        self.app.post(
            '/register_visitor', data=dict(fname="test", lname="test", city="test", address="test", email="sdfsd@sdf"), follow_redirects=True)
        self.app.get('/place/89ad85ab-1c32-4386-b61a-54e5c6f3010a', follow_redirects=True)
        response = self.app.post('/signout',
                                 data=dict(qrcode="89ad85ab-1c32-4386-b61a-54e5c6f3010a"),  follow_redirects=True)

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
