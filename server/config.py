import os


class BaseConfig(object):
    """ Base configuration. """
    DEBUG = False

class DevelopmentConfig(BaseConfig):
    """ Development configuration """
    DEBUG = True

class TestingConfig(BaseConfig):
    """ Testing configuration. 
    """
    DEBUG = True
    TESTING  = True

class ProductionConfig(BaseConfig):
    """Production configuration """
    DEBUG = False
