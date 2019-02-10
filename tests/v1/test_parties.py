""" Testing modules for parties """
import json
import unittest
from flask import json
from server import app

class TestParties(unittest.TestCase):
    """ Testing for parties """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.party_data = {
            "party_id" : 1,
            "name" :"party 1",
            "hq_address" : "Roysambu",
            "logo_url" : "https://file/1"
        }

    def test_createparty(self):
        """ Test for create party method """
        response = self.client.post(
            '/api/v1/admin/parties', data=json.dumps(self.party_data), 
            content_type='application/json')

        self.assertEqual(response.status_code, 201)

    def test_getallparties(self):
        """ Test for getting all parties method """
        response = self.client.get(
            '/api/v1/admin/parties', content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def getparty(self):
        """ Test for getting a specific party method """
        response = self.client.get(
            '/api/v1/admin/parties/<int:party_id>', data=json.dumps(self.party_data), 
            content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def editparty(self):
        """ Test for getting a specific party method """
        response = self.client.put(
            '/api/v1/admin/parties/<int:party_id>', data=json.dumps(self.party_data), 
            content_type='application/json')

        self.assertEqual(response.status_code, 200)

    def deleteparty(self):
        """ Test for getting a specific party method """
        response = self.client.delete(
            '/api/v1/admin/parties/<int:party_id>', data=json.dumps(self.party_data), 
            content_type='application/json')

        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
