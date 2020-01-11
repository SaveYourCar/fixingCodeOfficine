from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, SubmitField, BooleanField,  SelectField, RadioField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flaskblog.models import Post
import re

class PostForm(FlaskForm):
    nome = StringField('Nome')
    maschile = BooleanField('Maschile')
    femminile = BooleanField('Femminile')
    submit = SubmitField('Aggiungi Nome')

    def validate_nome(self, nome):
        if Post.query.filter_by(nome=nome.data.lower().capitalize()).first():
            raise ValidationError('questo nome esiste già')
        elif not bool(re.fullmatch(r'[a-zA-Z]+', nome.data)):
        	raise ValidationError('nome non valido')


class SearchForm(FlaskForm):
    nome = StringField('Nome')
    maschile = BooleanField('Maschile')
    femminile = BooleanField('Femminile')
    submit = SubmitField('Cerca Nome')

    def validate_nome(self, nome):
        if not Post.query.filter_by(nome=nome.data.lower().capitalize()).first():
            raise ValidationError('nome non presente')
        elif not bool(re.fullmatch(r'[a-zA-Z]+', nome.data)):
        	raise ValidationError('nome non valido')