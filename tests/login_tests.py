import json
#import tests


class ApiTestCase(SimpleTest):

    def test_hello_version(self):
        data = json.loads(self.app.test_client().get('/api/v0.1/users/me').get_data(as_text=True))
        assert data.get('email') == 'anEmail@hi.com'



