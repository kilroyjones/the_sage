import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    FINN_KEY = os.environ.get("FINN_KEY")
    SECRET_KEY = os.environ.get("SECRET_KEY")
