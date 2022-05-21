from waitress import serve

from app import app


try:
    serve(app, host='0.0.0.0', port=80, url_scheme='https')
except PermissionError as e:
    print('You must have super powers')
