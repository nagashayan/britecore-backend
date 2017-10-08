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

        self.feature = {'client_id':1,'title': 'Need filtering of data', 'description': 'should be able to filter to either order',
        'product_area':'sales','target_date':'7-22-2018'}
    
        # binds the app to the current context
        with self.app.app_context():
            # create all tables
            db.create_all()
    # executed after each test
    def tearDown(self):
        """teardown all initialized variables."""
        with self.app.app_context():
            # drop all tables
            db.session.remove()
            db.drop_all()

    def test_featuredetails_creation(self):
        """Test API can create a feature (POST request)"""
        res = self.client().post('/feature/', data=self.feature)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Need filtering of data', str(res.data))
   
    def test_featuredetails_getAll(self):
        """Test API can get a feature (after POST request)"""
        res = self.client().post('/feature/', data=self.feature)
        self.assertEqual(res.status_code, 201)
        self.assertIn('Need filtering of data', str(res.data))
        
        res = self.client().get('/feature/')
        self.assertEqual(res.status_code, 200)
        self.assertIn('Need filtering of data', str(res.data))
   
if __name__ == "__main__":
    unittest.main()