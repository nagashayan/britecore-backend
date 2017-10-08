import os
import unittest
from hello import app

class BasicTests(unittest.TestCase):
 
     # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = True

        self.app = app.test_client()
      
        self.assertEqual(app.debug, True)
 
    # executed after each test
    def tearDown(self):
        pass

    #initial test
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hello, World!')

if __name__ == "__main__":
    unittest.main()