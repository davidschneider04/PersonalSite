from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='html/templates') # this is our "WSGI application
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route("/")
def index():
    return render_template(f'base.html')

@app.route('/amanda')
def lam():
    return render_template('amanda.html')

@app.route('/plants')
def plants():
    return render_template('plants.html')


@app.route('/<pagenm>')
def please(pagenm):
    return render_template(f'{pagenm}.html')


# blueprints
#from app.auth.controllers import auth as auth_module
#app.register_blueprint(auth_module)

db.create_all()
