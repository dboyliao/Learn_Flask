from app import app
import unittest
import cPickle as pickle

#tester = app.test_client()

class FlaskTestCase(unittest.TestCase):
    
    # Ensure that flask was set up correctly.
    def test_index(self):
        tester = app.test_client()
        response = tester.get("/login", content_type = "html/text")
        self.assertEqual(response.status_code, 200)
    
    # Ensure that the login page load correctly.
    def test_login_page_load(self):
        tester = app.test_client()
        # record the attributes of a response of get method.
        response = tester.get("/login", content_type = "html/text")
        self.assertEqual("Please Login" in response.data, True)
        temp_dir = dict()
        for attr_name in dir(response):
            temp_dir[attr_name] = repr(response.__getattribute__(attr_name))
        with open("/Users/DboyLiao/Documents/flask_intro/response_get.pickle", "wb") as wf:
            pickle.dump(temp_dir, wf)
        # record the attributes of a testers. (thing can be tested)
        temp_dir = dict()
        for attr_name in dir(tester):
            temp_dir[attr_name] = repr(tester.__getattribute__(attr_name))
        with open("/Users/DboyLiao/Documents/flask_intro/tester.pickle", "wb") as wf:
            pickle.dump(temp_dir, wf)
        # record the attributes of a response of post method.
        response = tester.post("/login", data = dict(username = "admin", password = "admin"))
        temp_dir = dict()
        for attr_name in dir(response):
            temp_dir[attr_name] = repr(response.__getattribute__(attr_name))
        with open("/Users/DboyLiao/Documents/flask_intro/response_post.pickle", "wb") as wf:
            pickle.dump(temp_dir, wf)
    
    # Ensure the login behave correctly given the correct credentials
    def test_correct_login(self):
        tester = app.test_client()
        response = tester.post("/login",
                               data = {"username":"admin", "password":"admin"},
                               follow_redirects = True)
        self.assertIn(b"You were just logged in.", response.data)
    
    # Ensure the login behave correctly given the incorrect credentials
    def test_incorrect_login(self):
        tester = app.test_client()
        response = tester.post("/login",
                               data = {"username":"test", "password":"test"},
                               follow_redirects = True)
        self.assertIn("Please check the username or password.", response.data)
        #self.assertIn("Error: Invalid credentials. Please check the username or password.", response.data)
    
    # Ensure the logout behave correctly
    def test_logout(self):
        # Here we must initialize a new tester to preserve the loggin state.
        tester = app.test_client()
        tester.post("/login",
                    data = {"username":"admin", "password":"admin"},
                    follow_redirects = True)
        response = tester.get("/logout", follow_redirects = True)
        self.assertIn(b"You were just logged out.", response.data)
        
    # Ensure that the home requires login.
    def test_home_requires_login(self):
        tester = app.test_client()
        response = tester.get("/", follow_redirects = True)
        self.assertIn(b"You have to login first.", response.data)
        
    # Ensure the logout page requires login.
    def test_logout_requires_login(self):
        tester = app.test_client()
        response = tester.get("/logout", follow_redirects = True)
        self.assertIn(b"You have to login first.", response.data)
        
if __name__ == "__main__":
    unittest.main()