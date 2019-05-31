from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager
from flask_cors import CORS

from app import db, ma
from app.resources.user import UserResource, UserAuthResource, UsersResource
from app.resources.post import PostsResource, PostResource, PostsUserResource

class App():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile('config.py')
  api = Api(app)
  CORS(app)
  jwt = JWTManager(app)

  db.init_app(app)
  ma.init_app(app)

  api.add_resource(UserResource, '/user')
  api.add_resource(UsersResource, '/user/<int:_id>')
  api.add_resource(UserAuthResource, '/login')
  api.add_resource(PostsResource, '/posts')
  api.add_resource(PostsUserResource, '/posts/<int:_id>')
  api.add_resource(PostResource, '/post/<int:_id>')

  @classmethod
  def run_server(cls):
    cls.app.run()
