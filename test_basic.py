import os
import unittest
from app import create_app, db
from flask import json

class BasicTests(unittest.TestCase):
 
     # executed prior to each test
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app(config_name="testing")
        print(self.app)
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
    
    def test_feature_deletion(self):
        """Test API can delete an existing feature. (DELETE request)."""
        response = self.client().post(
            '/feature/',
            data=self.feature)
        self.assertEqual(response.status_code, 201)
        res = self.client().delete('/feature/1')
        self.assertEqual(res.status_code, 200)
        # Test to see if it exists, should return a 404
        result = self.client().get('/feature/1')
        self.assertEqual(result.status_code, 404)


    def test_api_can_get_feature_by_id(self):
        """Test API can get a single feature by using it's client_id."""
        response = self.client().post('/feature/', data=self.feature)
        self.assertEqual(response.status_code, 201)
        result_in_json = json.loads(response.data.decode('utf-8').replace("'", "\""))
        result = self.client().get('/feature/1')
        self.assertEqual(result.status_code, 200)
        self.assertIn('Need filtering of data', str(result.data))

    def test_feature_can_be_edited(self):
        """Test API can edit an existing feature. (PUT request)"""
        response = self.client().post(
            '/feature/',
            data=self.feature)
        self.assertEqual(response.status_code, 201)
        response = self.client().put(
            '/feature/1',
            data={
                'client_id': self.feature['client_id'],
                'title': 'Need enum filtering of data',
                'description': self.feature['description'],
                'target_date': self.feature['target_date'],
                'product_area': self.feature['product_area']
            })
        self.assertEqual(response.status_code, 200)
        results = self.client().get('/feature/1')
        self.assertIn('Need enum filtering of data', str(results.data))


if __name__ == "__main__":
    unittest.main()