""" Testing modules for offices """
import json
import unittest
from flask import json
import app

class TestOffices(unittest.TestCase):
    """ Testing for parties """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.office_data = {
            "office_id" : 1,
            "office_type" :"fed",
            "name" : "office1"
        }

    def test_createoffice(self):
        """ Test for create office method """
        response = self.client.post(
            '//api/v1/admin/createoffice', data=json.dumps(self.office_data), 
            content_type='application/json')
        self.assertEqual(response.json['office_id'], 1)
        self.assertEqual(response.json['office_type'], 'fed')
        self.assertEqual(response.json['name'], 'office1')
        self.assertEqual(response.status_code, 201)


    def test_getalloffices(self):
        """ Test for getting all parties method """
        response = self.client.get(
            '//api/v1/admin/offices/getall', data=json.dumps(self.office_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def getparty(self):
        """ Test for getting a specific party method """
        response = self.client.get(
            '/api/v1/admin/parties/get/<int:party_id>', data=json.dumps(self.office_data), 
            content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def editoffice(self):
        """ Test for getting a specific party method """
        response = self.client.post(
            '/api/v1/admin/offices/get/<int:office_id>', data=json.dumps(self.office_data), 
            content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
