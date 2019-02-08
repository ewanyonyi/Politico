""" Testing modules for parties """
import unittest
import json
from flask import json
import app

class TestParties(unittest.TestCase):
    """ Testing for parties """
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.data = {
            "tittle": "Religion is all about faith",
            "description": "Some serious and useful content here"
        }
        self.party_data = {
            "id" : 1,
            "name" :"party 1",
            "hgAddress" : "Roysambu",
            "logoUrl" : "https://file/1"
        }

    def test_createparty(self):
        """ Test for create party method """
        response = self.client.post(
            '/api/v1/admin/createparty', data=json.dumps(self.party_data),
            content_type='application/json')
        self.assertEqual(response.status_code, 201)

if __name__ == '__main__':
    unittest.main()
