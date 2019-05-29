from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, create_access_token,get_jwt_identity
from app.models.User import UserModel
from flask import jsonify, make_response
from app.models import db

from datetime import datetime as dt

class UserResource(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email', type=str, help="Campo não pode ser vazio")
  parser.add_argument('password', type=str, help="Campo não pode ser vazio")

  @jwt_required
  def get(self):
    return get_jwt_identity()

  def post(self):
    args = self.parser.parse_args()
    user = UserModel.find_by_email(args['email'])
    if not user:
      new_user = UserModel(email=args['email'], password=args['password'], created_at=dt.now())

      db.session.add(new_user)
      db.session.commit()

      return { "message": "Usuário criado com sucesso" }, 200
    else:
      return { "message": "Já existe um usuário com este email" }, 400

class UserAuthResource(Resource):
  parser = reqparse.RequestParser()
  parser.add_argument('email', type=str, help="Campo não pode ser vazio")
  parser.add_argument('password', type=str, help="Campo não pode ser vazio")

  def post(self):
    args = self.parser.parse_args()
    user = UserModel.find_by_email(args['email'])

    if user and user.check_password(args['password']):
      access_token = create_access_token(identity={'email': args['email'], 'id': user.id})
      return make_response(jsonify({'token': access_token}), 200)