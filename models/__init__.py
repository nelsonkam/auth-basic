from orator import DatabaseManager, Model
from orator.orm import has_many, belongs_to, has_one, belongs_to_many
import config

db = DatabaseManager(config.DATABASES)
Model.set_connection_resolver(db)


class User(Model):
  __hidden__ = ['password']