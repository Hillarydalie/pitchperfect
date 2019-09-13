from flask import Flask
from config import Config
from flask_login import login_manager,LoginManager
from flask_sqlalchemy import SQLAlchemy

app =  Flask(__name__)
# Initialise DB
db = SQLAlchemy(app)
# initialise login manager
login_manager = LoginManager(app)
# Redirect to the login page
login_manager.login_view = "auth.login"
# Change how secret kkey is generated
login_manager.session_protection = "strong"

def create_app():
    app.config.from_object(Config)
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)
    return app
    