from flask import Flask
from config import Config
from flask_login import login_manager,LoginManager
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app =  Flask(__name__)
bootstrap = Bootstrap()
# Initialise DB
db = SQLAlchemy(app)
mail = Mail()
# initialise login manager
login_manager = LoginManager(app)
# Redirect to the login page
login_manager.login_view = "auth.login"
# Change how secret kkey is generated
login_manager.session_protection = "strong"

def create_app(config_name):
    app.config.from_object(configurations[config_name])
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint    
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    return app
    