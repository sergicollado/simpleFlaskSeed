from flask.ext.restplus import Resource, Api, fields
from app import api, namespace
from app.users.userDb import User

@namespace.route('/users/me')
@api.doc(responses={404: 'Todo not found'}, params={'token': 'aToken'})
class GetUser(Resource):
    def get(self):
        return {
            'cards': ['aCard','anotherCard'],
            'email': 'anEmail@hi.com'
        }

fields = {
    'username': fields.String,
    'email': fields.String,
}

@namespace.route('/users/first')
@api.doc(responses={404: 'Todo not found'}, params={'token': 'aToken'})
class GetFirstUser(Resource):


    @api.marshal_with(fields)
    def get(self):
        return  User.getFirstUser()
