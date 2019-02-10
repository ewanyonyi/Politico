""" Server initialization module """
import os
from flask import Flask
from api.v1.auth.auth_views import AUTH_API_BLUEPRINT
from api.v1.admin.admin_views import ADMIN_API_BLUEPRINT

app = Flask(__name__)

SERVER_SETTINGS = os.getenv(
    'APP_SETTINGS',
    'develop.config.DevelopmentConfig'
)

app.config.from_object('develop.config.DevelopmentConfig')

app.register_blueprint(AUTH_API_BLUEPRINT, url_prefix='/api/v1')
app.register_blueprint(ADMIN_API_BLUEPRINT, url_prefix='/api/v1')
