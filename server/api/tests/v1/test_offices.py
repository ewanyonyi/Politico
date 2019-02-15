""" Testing modules for offices """
import json
import unittest
from flask import json
from server import app

class TestOffices(unittest.TestCase):
    """ Testing for parties """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.office_data = {
            "office_id" : 1,
            "office_type" :"Federal",
            "name" : "office1"
        }

    def test_createoffice(self):
        """ Test for create office method """
        response = self.client.post(
            '/api/v1/offices', data=json.dumps(self.office_data), 
            content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, 200)


    def test_getalloffices(self):
        """ Test for getting all offices method """
        response = self.client.get('/api/v1/offices')
        print(response)
        self.assertEqual(response.status_code, 200)

    def getoffice(self):
        """ Test for getting a specific party method """
        response = self.client.get(
            '/api/v1/parties/get/<int:party_id>', content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def editoffice(self):
        """ Test for getting a specific party method """
        response = self.client.post(
            '/api/v1/offices/<int:office_id>', data=json.dumps(self.office_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
