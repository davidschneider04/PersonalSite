from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__,
        template_folder='html/templates',
        static_url_path='',
        static_folder='html/static')
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/davesdatadepot/<project>')
def singleproj(project):
    return render_template([f'{project}.html', '404.html'])


@app.route('/davesdatadepot')
def projects():
    def create_project(pname, purl, desc):
	    return {'project':pname, 'reflink':purl, 'description': desc}
    projects = []
    projects.append(create_project(
        "FindScene — App to Find Video Links",
        "findscene",
        "Do you have a favorite line from a favorite TV show or movie, but don't remember what episode or time it's from? Let FindScene find the exact spot and link you to it."
        ))
    projects.append(create_project(
        "Mapping Colorado Mountains",
        "mapping_mountains",
        "Using Python with Folium to create an interactive map of the 100 highest peaks in Colorado."
        ))
    projects.append(create_project(
        "Code For This Website",
        "website_code",
        "So meta. Tools and strategies used for deploying and hosting."
        ))
    return render_template('davesdatadepot.html', context=projects)


@app.route('/<pagenm>')
def pages(pagenm):#, subpg):
    if not pagenm:
        pagenm = 'home'
    #if not subpg:
    #    path = pagenm+'.html'
    #else:
    #    path = pagenm+'/'+subpg+'.html'
    path = pagenm+'.html'
    return render_template([path, '404.html'])


# blueprints
#from app.auth.controllers import auth as auth_module
#app.register_blueprint(auth_module)

db.create_all()
