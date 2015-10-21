from flask.ext.testing import TestCase
import app

def create_app():
    app.app.config['TESTING'] = True
    app.app.config.from_object('config.config_tests')
    return app.app


class SimpleTest(TestCase):

    def create_app(self):
        return create_app()



class DbTest(SimpleTest):

    SQLALCHEMY_DATABASE_URI = "sqlite://something"
    TESTING = True
    db = app.db


    def setUp(self):

        self.db.create_all()

    def tearDown(self):

        self.db.session.remove()
        self.db.drop_all()
