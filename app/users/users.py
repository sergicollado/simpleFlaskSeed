from flask import Blueprint
from flask_restful import Resource, Api

api_bp = Blueprint('users', __name__)


class GetUser(Resource):
    def get(self):
        return {
            'cards': ['aCard','anotherCard'],
            'email': 'anEmail@hi.com'
        }

api = Api(api_bp)
api.add_resource(GetUser, '/users/me')
