""" Users Module tests """
import json
import unittest
from flask import json
from develop import app

class TestUsers(unittest.TestCase):
    """ User testing class """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.user_data = {
            "id":1,
            "firstname":"Emanuel",
            "lastname":"Wanyonyi",
            "othername":"Dickson",
            "email":"joe@gmail.com",
            "phone_nember":"070000000000",
            "passport_url":"http://files/log1",
            "is_admin":True,
            "password":"Sample@1234"
        }

    def test_siginup(self):
        """ Test for user sigining """
        response = self.client.post(
            '/api/v1/auth/signup', data=json.dumps(self.user_data), 
            content_type='application/json')
        data = json.loads(response.data)
        self.assertEqual(data["status"], 201)
        

    def test_siginin(self):
        """ Test for login of registered-user login """
        response = self.client.post(
            '/api/v1/auth/signin', data=json.dumps(self.user_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
