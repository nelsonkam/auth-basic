from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from validators import UserSchema
from models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_refresh_token_required, get_jwt_identity

blueprint = Blueprint("auth", __name__, url_prefix="/auth")
bcrypt = Bcrypt()

@blueprint.route('/login', methods=['POST'])
def login():
  data = request.get_json()
  if data:
    user = User.where('email', data.get('email')).first()
    if user and bcrypt.check_password_hash(user.password, data.get('password') or ''):
      tokens = {
        'access_token': create_access_token({'email': user.email}),
        'refresh_token': create_refresh_token({'email': user.email})
      }
      return jsonify(tokens), 200
  return jsonify({'errors': {'login': 'Please check your credentials and try again.'}}), 401

@blueprint.route('/register', methods=['POST'])
def register():
  data = request.get_json()
  data, errors = UserSchema().load(data)
  if errors:
    return jsonify({'errors': errors}), 400
  else:
    user = User()
    user.name = data['name']
    user.email = data['email']
    user.password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user.save()
    return jsonify(user.serialize()), 200
  

@blueprint.route('/refresh', methods=['POST'])
@jwt_refresh_token_required
def refresh():
  identity = get_jwt_identity()
  token = {
      'access_token': create_access_token(identity=identity)
  }
  return jsonify(token), 200