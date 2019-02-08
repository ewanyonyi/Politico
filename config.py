import os


class BaseConfig(object):
    """ Base configuration. """
    SECRET_KEY = os.getenv('SECRET_KEY', 'this_is_secret')
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    DEBUG = True

class TestingConfig(BaseConfig):
    """ Testing configuration. 
    """
    DEBUG = True
    TESTING  = True
    PRESERVE_CONTEXT_ON_EXCEPTION = False

class ProductionConfig(BaseConfig):
    """Production configuration """
    SECRET_KEY = 'this_is_secret'
    DEBUG = False