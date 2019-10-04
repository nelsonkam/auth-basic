from marshmallow import Schema, ValidationError, fields, validates_schema, validates
from models import User

class UserSchema(Schema):
  email = fields.Email(required=True)
  name = fields.Str(required=True)
  password=fields.Str(required=True)
  confirm=fields.Str(required=True)

  @validates_schema
  def validate_confirm(self, data):
    if data.get('password') != data.get('confirm'):
      raise ValidationError("Value doesn't match password", 'confirm')
  
  @validates('email')
  def validate_email(self, value):
    if User.where('email', value).first():
      raise ValidationError('Email address already taken')