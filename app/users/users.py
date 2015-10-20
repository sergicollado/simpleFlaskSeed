from flask.ext.restplus import Resource, Api
from app import api, namespace


@namespace.route('/users/me')
@api.doc(responses={404: 'Todo not found'}, params={'token': 'aToken'})
class GetUser(Resource):
    def get(self):
        return {
            'cards': ['aCard','anotherCard'],
            'email': 'anEmail@hi.com'
        }

