import os
import unittest
from app import create_app, db

class BasicTests(unittest.TestCase):
 
     # executed prior to each test
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        self.client = self.app.test_client
        
        self.assertEqual(self.app.debug, True)

        self.feature = {'title': 'Need filtering of data', 'description': 'should be able to filter to either order','product_area':'sales','target_date':'22/7/2018'}
    
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()
    # executed after each test
    def tearDown(self):
        pass

   
if __name__ == "__main__":
    unittest.main()