from waitress import serve

from app import app


serve(app, listen='*:8080') #host='0.0.0.0', port=8080)
