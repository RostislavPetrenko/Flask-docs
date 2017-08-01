import os
class Configuration():
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s/blog.db?check_same_thread=False' % APPLICATION_DIR