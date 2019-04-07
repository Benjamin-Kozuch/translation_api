import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    YANDEX_KEY = os.environ.get('YANDEX_KEY') or 'trnsl.1.1.20190405T175806Z.c574738784a00216.aa58f2d2a32f999e3e95b2b4eb651a7320dd9bd9'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False