import os, sys
import string
import random
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import tempfile
import unittest

from app import app


class FlaskTestCase(unittest.TestCase):
    
    # Test of home page if it opens succesfully
    def test_homepage(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type="html/text")
        self.assertIn(b'Home Page', response.data)
        
    # Test of registration page if it opens succesfully    
    def test_registration(self):
        tester = app.test_client(self)
        response = tester.get('/registration', content_type="html/text")
        self.assertIn(b'Registration Page', response.data)    
    
    # Test of login page if it opens succesfully    
    def test_login(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type="html/text")
        self.assertIn(b'Login Page', response.data)    
    
    # Test of upload page if it opens succesfully    
    def test_upload(self):
        tester = app.test_client(self)
        response = tester.get('/upload', content_type="html/text")
        self.assertIn(b'Upload Page', response.data)    
    
    # Test of scan page if it opens succesfully    
    def test_scan(self):
        tester = app.test_client(self)
        response = tester.get('/scan', content_type="html/text")
        self.assertIn(b'Scan Page', response.data)    
    
    #def test_instructor_registration_successful(self):
        #tester = app.test_client(self)
        #response = tester.post('/login', data=dict(user_firstname="Idris", user_phoneno="017685156567", user_emailadd="i.chendid@jacobs-university.de", user_address="NB-116, Nordmetall", user_lastname="Chendid" ), follow_redirects=True)
        #self.assertIn(b'Invalid Credentials!', response.data)   
        
if __name__=='__main__':
   unittest.main()        