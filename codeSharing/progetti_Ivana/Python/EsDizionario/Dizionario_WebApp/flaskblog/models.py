from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(20), unique=True, nullable=False)
    genere = db.Column(db.Boolean() , nullable=False)

    def __repr__(self):
        return f"Post('{self.id}','{self.nome}', '{self.genere}')"
