from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__, template_folder='templates') # this is our "WSGI application"
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/plants/')
def plants():
    return render_template('plants.html')

@app.route("/")
def index():
    return render_template(f'index.html')

# blueprints
#from app.auth.controllers import auth as auth_module
#app.register_blueprint(auth_module)

db.create_all()
