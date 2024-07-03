from flask_script import Manager
from flask import Flask
app = Flask(__name__)
manager = Manager(app)

@manager.option('-n', '--name', dest='name', default='Flask')
def hello(name):
    print(f'Hello,{name}')

@manager.option('-u', '--username', dest='username', default='admin')
@manager.option('-p', '--pwd', dest='pwd', default='123456')
def login(username,pwd):
    print(f'用户名,{username}')
    print(f'密码,{pwd}')

if __name__ == '__main__':
    manager.run()
