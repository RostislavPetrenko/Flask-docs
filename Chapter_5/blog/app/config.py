import os
class Configuration():
    APPLICATION_DIR = os.path.dirname(os.path.realpath(__file__))
    DEBUG = True
    SECRET_KEY = 'VtA3YkXGcs4kWzWb' #Создайте уникальный ключ
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:secretpassword@localhost:5432/blog_db'
    STATIC_DIR = os.path.join(APPLICATION_DIR, 'static')
    IMAGES_DIR = os.path.join(STATIC_DIR, 'images')
