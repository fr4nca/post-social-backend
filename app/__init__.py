from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager

from .models import db
from .resources.user import UserResource, UserAuthResource

def create_app():
  app = Flask(__name__, instance_relative_config=True)
  app.config.from_pyfile('config.py')
  api = Api(app)
  jwt = JWTManager(app)

  db.init_app(app)

  api.add_resource(UserResource, '/user')
  api.add_resource(UserAuthResource, '/login')

  return app
