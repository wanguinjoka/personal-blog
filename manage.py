from app import create_app,db
from app.models import Follower
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand


# Creating app instance
# app = create_app('production')
app = create_app('development')

manager = Manager(app)

migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)


manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict(app = app,db = db, Follower = Follower )

if __name__ == '__main__':
    manager.run()
