from orator.seeds import Seeder
from flask_bcrypt import Bcrypt
from models import User

bcrypt = Bcrypt()

class UsersTableSeeder(Seeder):
    def run(self):
        """
        Run the database seeds.
        """
        self.factory.register(User, self.users_factory)
        self.factory(User, 10).create()

    def users_factory(self, faker):
        return {
            'name': faker.name(),
            'email': faker.email(),
            'password': bcrypt.generate_password_hash(data['password']).decode('utf-8')
        }

