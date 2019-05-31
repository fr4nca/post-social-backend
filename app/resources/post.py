from datetime import datetime as dt

from flask import jsonify, make_response
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from app import db
from app.models.User import UserModel
from app.models.Post import PostModel, posts_schema, post_schema

user_parser = reqparse.RequestParser()
user_parser.add_argument('corpo', type=str, help='Campo não pode ser vazio')
user_parser.add_argument('titulo', type=str, help='Campo não pode ser vazio')
user_parser.add_argument('tb_user_id', type=str, help='Campo não pode ser vazio')

class PostsResource(Resource):
  def get(self):
    res = PostModel.query.order_by(PostModel.created_at.desc()).all()
    posts = posts_schema.dump(res)
    return posts

  @jwt_required
  def post(self):
    args = user_parser.parse_args()
    new_post = PostModel(corpo=args['corpo'], titulo=args['titulo'], tb_user_id=args['tb_user_id'], created_at=dt.now())

    db.session.add(new_post)
    db.session.commit()

    new_post = post_schema.dump(new_post)
    return new_post
    
class PostResource(Resource):
  @jwt_required
  def delete(self, _id):
    res = PostModel.find_by_id(_id)
    if res:
      post = post_schema.dump(res)
      db.session.delete(res)
      db.session.commit()
      return post
    else:
      return { 'message': 'Nenhum post com este id' }, 400  


  def get(self, _id):
    res = PostModel.find_by_id(_id)

    if res:
      post = post_schema.dump(res)
      return post
    else:
      return { 'message': 'Nenhum post com este id' }, 400

class PostsUserResource(Resource):
  @jwt_required
  def get(self, _id):
    user = UserModel.find_by_id(_id)
    if user:
      res = PostModel.find_all_by_user(user)
      posts = posts_schema.dump(res)
      return posts
    else:
      return { 'message': 'Nenhum usuário com este id' }, 400
