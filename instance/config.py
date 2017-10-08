import os

class Config(object):
    """Parent configuration class."""
    DEBUG = True
    CSRF_ENABLED = True
    SECRET = "britecore-project-by-nagashayan"
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/britecore_api"

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class TestingConfig(Config):
    """Configurations for Testing, with a separate test database."""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost:5432/test_db'
    DEBUG = True

app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig
}