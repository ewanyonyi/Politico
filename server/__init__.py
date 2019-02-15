""" Server initialization module """
import os
from flask import Flask

app = Flask(__name__)

SERVER_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'server.config.DevelopmentConfig'
)

app.config.from_object('server.config.DevelopmentConfig')

from server.api.v1.views.office import office_api_v1_blueprint
from server.api.v1.views.party import party_api_v1_blueprint

app.register_blueprint(office_api_v1_blueprint, url_prefix='/api/v1')
app.register_blueprint(party_api_v1_blueprint, url_prefix='/api/v1')
