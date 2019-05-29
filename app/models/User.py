from . import db
from werkzeug.security import generate_password_hash, check_password_hash

class UserModel(db.Model):
    __tablename__ = 'tb_user'
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(80), index=True, unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_at = db.Column(db.String(80), nullable=False)

    def __init__(self, email, password, created_at):
        self.email = email
        self.password = self.set_password(password)
        self.created_at = created_at

    def set_password(self, password):
        return generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @classmethod
    def find_by_email(cls, email):
        user = cls.query.filter_by(email=email).first()
        return user

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def __str__(self):
        return 'User(email='+self.email+', id='+str(self.id)+ ')'

    def __repr__(self):
        return {'email':self.email, 'id':self.id}