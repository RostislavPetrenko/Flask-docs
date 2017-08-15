from flask import Flask, g
from flask.ext.login import LoginManager, current_user
from flask.ext.migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.bcrypt import Bcrypt
from config import Configuration



app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config.from_object(Configuration)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Добавьте в самый конец модуля
login_manager = LoginManager(app)
login_manager.login_view = "login"
@app.before_request
def _before_request():
    g.user = current_user