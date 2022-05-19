import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__)) 
SECRET_KEY = "secret" # TODO: replace with an actual secret key
SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'app.db')}"
DATABASE_CONNECT_OPTIONS = {}

THREADS_PER_PAGE = 2
CSRF_ENABLED = True # cross site request forgery protection
CSRF_SESSION_KEY = SECRET_KEY

DEBUG = True
