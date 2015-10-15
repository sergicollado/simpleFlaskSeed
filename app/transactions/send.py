from flask import Blueprint
from flask_restful import Resource, Api, reqparse

api_bp = Blueprint('transactions', __name__)


class Send(Resource):
    def parse(self):
        parser = reqparse.RequestParser()

        parser.add_argument('amount', required=True, type=str,
                            help="Amount cannot be blank!")

        parser.add_argument('card', required=True, type=str,
                            help="Card cannot be blank!")

        parser.add_argument('text', required=False, type=str,
                            help="text description")

        return parser.parse_args()

    def post(self):

        args = self.parse()
        print(args)
        return {'transaction': 'aTransactionId'}

api = Api(api_bp)
api.add_resource(Send, '/transactions/send')

