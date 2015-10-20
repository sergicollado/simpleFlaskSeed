from tests.login_tests import *
from flask.ext.testing import TestCase
import app


def create_app():
    app.app.config['TESTING'] = True
    return app.app


class SimpleTest(TestCase):

	def create_app(self):
		return create_app()


class DbTest(SimpleTest):

    SQLALCHEMY_DATABASE_URI = "sqlite://"
    TESTING = True


    def setUp(self):

        db.create_all()

    def tearDown(self):

        db.session.remove()
        db.drop_all()
