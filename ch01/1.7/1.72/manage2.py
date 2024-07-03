from flask_script import Manager,Server
from flask import Flask
app=Flask(__name__)
manager=Manager(app)
manager.add_command("runserver", Server(use_debugger=True))

if __name__=="__main__":
    manager.run()