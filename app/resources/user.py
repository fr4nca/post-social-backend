from datetime import datetime as dt

from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity

from app import db
from app.models.User import UserModel, user_schema

user_parser = reqparse.RequestParser()
user_parser.add_argument('email', type=str, help='Campo não pode ser vazio')
user_parser.add_argument('name', type=str, help='Campo não pode ser vazio')
user_parser.add_argument('password', type=str, help='Campo não pode ser vazio')

class UserResource(Resource):
  @jwt_required
  def get(self):
    return get_jwt_identity()

  def post(self):
    args = user_parser.parse_args()
    user = UserModel.find_by_email(args['email'])
    if not user:
      new_user = UserModel(email=args['email'], password=args['password'], name=args['name'], created_at=dt.now())

      db.session.add(new_user)
      db.session.commit()

      return { 'message': 'Usuário criado com sucesso' }, 200
    else:
      return { 'message': 'Já existe um usuário com este email' }, 400

class UserAuthResource(Resource):
  @classmethod
  def post(cls):
    args = user_parser.parse_args()
    user = UserModel.find_by_email(args['email'])

    if user and user.check_password(args['password']):
      access_token = create_access_token(identity={ 'email': args['email'], 'id': user.id })
      return { 'token': access_token }, 200
    else:
      return { 'message': 'Credenciais invalidas'}, 401

class UsersResource(Resource):
  @jwt_required
  def get(self, _id):
    user = UserModel.find_by_id(_id)
    user = user_schema.dump(user)
    if user:
      return user
    else:
      return { 'message': 'Usuário não existe com este id' }, 400