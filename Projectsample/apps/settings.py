"""
settings.py

Configuration for Flask app

"""
import os
from datetime import timedelta

class Config(object):
    # Set secret key to use session
    SECRET_KEY = "likelion-flaskr-secret-key"
    debug = False
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=60)


class Production(Config):
    debug = True
    CSRF_ENABLED = False
    ADMIN = "goodmorningpg1@gmail.com"
    SQLALCHEMY_DATABASE_URI = 'mysql+gaerdbms:///blog?instance=goodmorning-page:mymornings'
    migration_directory = 'migrations'

