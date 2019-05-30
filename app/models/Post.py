from app.server import db, ma
from app.models.User import UserSchema

class PostModel(db.Model):
  __tablename__ = 'tb_post'
  id = db.Column(db.Integer, primary_key=True)
  corpo = db.Column(db.String(200), nullable=False)
  titulo = db.Column(db.String(100), nullable=False)
  tb_user_id = db.Column(db.Integer, db.ForeignKey('tb_user.id'), nullable=False)
  created_at = db.Column(db.String(80), nullable=False)

  def __init__(self, corpo, titulo, tb_user_id, created_at):
    self.tb_user_id = tb_user_id
    self.corpo = corpo
    self.titulo = titulo
    self.created_at = created_at

  @classmethod
  def find_all_by_user(cls, user):
    return user.posts

  @classmethod
  def find_by_id(cls, _id):
    return cls.query.filter_by(id=_id).first()

class PostSchema(ma.Schema):
  class Meta:
    fields=('id', 'corpo', 'titulo', 'tb_user_id', 'created_at', 'user')
  user = ma.Nested(UserSchema)

post_schema = PostSchema()
posts_schema = PostSchema(many=True)