from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.restplus import Api

app = Flask(__name__)
app.config.from_object('config.config')
api = Api(app, version=app.config['VERSION'], title='api title',
              description='Api description'
          )
namespace = api.namespace(app.config['URL_PREFIX'], description='version api')

db = SQLAlchemy(app)
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)

from app.users import userDb, users, login
from app.transactions import send
