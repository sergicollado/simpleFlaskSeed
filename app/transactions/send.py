from flask.ext.restplus import  Resource
from app import api, namespace

parser = api.parser()
parser.add_argument('amount', required=True, type=str,location='form',
                    help="Amount cannot be blank!")
parser.add_argument('card', required=True, type=str,location='form',
                    help="Card cannot be blank!")
parser.add_argument('text', required=False, type=str,location='form',
                            help="text description")


@namespace.route('/transactions/send')
@api.doc(params={'amount': 'aToken', 'card':'aCard'})
class Send(Resource):

    @api.doc(parser=parser)
    def post(self):
        '''Send a transaction '''
        args = parser.parse_args()
        return {'transaction': args}


