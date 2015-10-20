from flask.ext.restplus import Resource
from app import api, namespace

parser = api.parser()
parser.add_argument('idCard', required=True, type=str, location='form',
                    help="IdCard cannot be blank!")

@namespace.route('/login')
@api.doc(params={'idCard':'Idenfitication document'})
class Login(Resource):

    @api.doc(parser=parser)
    def post(self):
        '''Login user into platform'''
        args =parser.parse_args()
        return {
            'user':args
        }

