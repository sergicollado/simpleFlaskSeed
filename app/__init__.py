from flask import Flask
from app.users.users import api_bp
from app.transactions.send import api_bp as send_api
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_object('config')

app.register_blueprint(api_bp)
app.register_blueprint(send_api)


db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.users import userDb
