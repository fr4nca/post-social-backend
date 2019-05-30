
from flask import Flask
from flask_restful import Api, Resource
from flask_jwt_extended import JWTManager

from app import db
from app import ma
from app.resources.user import UserResource, UserAuthResource
from app.resources.post import PostsResource, PostResource, PostsUserResource

app = Flask(__name__, instance_relative_config=True)
app.config.from_pyfile('config.py')
api = Api(app)
jwt = JWTManager(app)

db.init_app(app)
ma.init_app(app)

api.add_resource(UserResource, '/user')
api.add_resource(UserAuthResource, '/login')
api.add_resource(PostsResource, '/posts')
api.add_resource(PostsUserResource, '/posts/<int:_id>')
api.add_resource(PostResource, '/post/<int:_id>')
