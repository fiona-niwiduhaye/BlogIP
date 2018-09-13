from app import create_app
from flask_script import Manager, Server

# import the create app funtion from app and create an instance of the entire app while passing in the cofiguration settings in the parameters of the funtion
app = create_app('development')

manager = Manager(app)

# add command for running the server using manager
manager.add_command('server', Server)


if __name__ == '__main__':
    manager.run()
