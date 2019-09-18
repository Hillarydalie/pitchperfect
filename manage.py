from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app,db
from app.models import User

# app = create_app()
app = create_app('production')

manager =  Manager(app)
# Initiate the migrate we import
migrate = Migrate(app,db)
manager.add_command('runserver',Server(use_debugger=True))
# Initiate the migrate command, and name how we call it. Here we do db
manager.add_command('db',MigrateCommand)



@manager.shell
def add_shell_context():
    return {"db":db,"User":User}

if __name__=="__main__":
    manager.run()