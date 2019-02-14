""" Server initialization module """
import os
from flask import Flask
from server.api.v1.admin.admin_views import admin_api_v1_blueprint

app = Flask(__name__)

SERVER_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'server.config.DevelopmentConfig'
)

app.config.from_object('server.config.DevelopmentConfig')

app.register_blueprint(admin_api_v1_blueprint, url_prefix='/api/v1')
