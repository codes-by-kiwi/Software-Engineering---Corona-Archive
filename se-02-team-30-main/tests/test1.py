try: 
    import app as app
    import unittest
    
except Exception as e:
    print("Some pre-requisite modules are missing! {}".format(e))
    
class AntiCoronaTests(unittest.TestCase):
    
    #Tests that run successfully: 8
    #Tests that failed: 3
    
    # having a test case to see if the landing page has code 200 -successful
    def test_landing_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        #checks if landing page contains the phrase "Protect yourself..."
        self.assertIn(b"Protect yourself", result.data)
    
    #check for what the page returns as content type
    def test_landing_page_content(self):
        checker = app.app.test_client(self)
        result = checker.get("/")
        self.assertEqual(result.content_type, "text/html; charset=utf-8")
    
    # having a test case for page - succesful or not
    def test_register_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/register", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        #checks if info page contains the phrase "Hello..."
        self.assertIn(b"Hello", result.data)
        
    # having a test case for page - succesful or not
    def test_hospital_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/hospitalRegister", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        
    # having a test case for page - succesful or not
    def test_visitor_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/visitorRegister", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        
    # having a test case for page - succesful or not
    def test_place_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/placeRegister", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
    
    # having a test case for page - succesful or not
    def test_agent_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/agentRegister", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        
    # having a test case for page - succesful or not
    def test_guide_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/moreinfo", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        #checks if info page contains the phrase "infection status..."
        self.assertIn(b"infection status", result.data)
        
    # having a test case for page - succesful or not
    def test_certificate_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/uploadImage", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        #checks if page contains the phrase "Chosen file..."
        self.assertIn(b"Chosen file...", result.data)
        
    # having a test case for page - succesful or not
    def test_QR_page(self):
        checker = app.app.test_client(self)
        result = checker.get("/QRcodegenerator", content_type="html/text")
        status = result.status_code
        self.assertEqual(status, 200)
        #checks if page contains the phrase "Fight Corona.."
        self.assertIn(b"Fight Corona..", result.data)
        
    #test for registered places 
    def test_visitorresponse(client):
        response = client.get("/place_name")
        assert b"<h2>Jacobs</h2>" in response.data

if __name__ == '__main__':
    unittest.main()