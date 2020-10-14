import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '736473878247193475827'
