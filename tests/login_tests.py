import json
from tests.base import SimpleTest, DbTest
from app.users.userDb import User

class ApiTestCase(SimpleTest):

    def test_hello_version(self):
        data = json.loads(self.app.test_client().get('/api/v0.1/users/me').get_data(as_text=True))
        assert data.get('email') == 'anEmail@hi.com'

class ApiDbTestCase(DbTest):

    username = 'anUsername'
    email = 'anEmail'

    def test_lookup(self):

        user = User(username=self.username, email=self.email)
        self.db.session.add(user)
        self.db.session.commit()

        # this works
        assert user in self.db.session

        data = json.loads(self.app.test_client().get('/api/v0.1/users/first').get_data(as_text=True))
        assert data.get('email') == self.email
