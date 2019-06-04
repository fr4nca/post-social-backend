import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = 'Sm9obiBTY2hyb20ga2lja3MgYXNz'
JWT_SECRET_KEY = 'AOJ986asd8A&sj97s9AJs80asajaSa876a8s7A'
JWT_ACCESS_TOKEN_EXPIRES = False
SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(basedir, 'db.sqlite')
SQLALCHEMY_TRACK_MODIFICATIONS=False
DEBUG = False