# Server configuration module """
# Server config file
import os

import os
POSTGRES = {
    'user': 'Emanuel',
    'pw': '1234',
    'db': 'politico_db',
    'host': 'localhost',
    'port': '5432'
}

class BaseConfig(object):
    """ Base configuration. """
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_key')
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

class TestingConfig(BaseConfig):
    """ Testing configuration. 
    """
    DEBUG = True
    TESTING  = True
    #SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test'
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(BaseConfig):
    """Production configuration """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql:///url_for_database'
