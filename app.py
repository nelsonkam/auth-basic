from flask import Flask
from flask_jwt_extended import JWTManager
from flask_cors import CORS
import config
from services import auth, upload

app = Flask(__name__)
app.config.from_pyfile('config.py')
jwt = JWTManager(app)
CORS(app)
app.register_blueprint(auth.blueprint)
app.register_blueprint(upload.blueprint)

if __name__ == "__main__":
  app.run(debug=True)