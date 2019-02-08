""" Users Module tests """
import json
import unittest
from flask import json
import app

class TestUsers(unittest.TestCase):
    """ User testing class """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.user_data = {
            "email":"joe@gmail.com",
            "password":"123456",
        }

    def test_siginup(self):
        """ Test for user registration """
        response = self.client.post(
            '/auth/signup', data=json.dumps(self.user_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_siginin(self):
        """ Test for login of registered-user login """
        response = self.client.post(
            '/auth/signin', data=json.dumps(self.user_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
