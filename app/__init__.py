from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__) # this is our "WSGI application"
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def index():
    poop = "A BEAUTIFUL FLOWER"
    return render_template('index.html', **locals())

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


# blueprints
from app.auth.controllers import auth as auth_module
app.register_blueprint(auth_module)

db.create_all()
