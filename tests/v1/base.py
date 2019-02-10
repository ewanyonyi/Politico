""" This the base testing """
# develop/tests/v1/base.py

from flask_testing import TestCase
from server import app


class BaseTestCase(TestCase):
    """ Base Tests """

    def create_app(self):
        """ Test for creating an app """
        app.config.from_object('server.config.TestingConfig')
        return app
