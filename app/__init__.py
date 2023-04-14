import os
import shutil
from flask import Flask
from flask_login import LoginManager
from app.models.user import User
from app import cli
from app import database
from app import views


login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()

def create_app(config="instance.config.DevelopmentConfig"):
    # Create and configure the app
    flask_app = Flask(__name__, instance_relative_config=True, template_folder='./templates')

    # Ensure the instance folder with the deployment configuration is available
    try:
        os.makedirs(flask_app.instance_path)

        src_dir = os.path.join(flask_app.root_path,'..','config.py.example')
        dst_dir = os.path.join(flask_app.instance_path,'config.py')
        shutil.copy(src_dir,dst_dir)

        flask_app.logger.error('''The instance path was now created and a sample config file has been generated.
        Modify this file to suit your instance needs.
        
        The file location is at <project root>/instance/config.py
         ''')
    except OSError:
        pass
    finally:
        flask_app.config.from_object(config)

    #Initialise our db
    database.init_app(flask_app)

    #Initialise our cli
    cli.init_app(flask_app)

    #Initialise flask login
    login_manager.init_app(flask_app)

    # Initialse our views and controllers for our app
    views.init_app(flask_app)

    return flask_app
