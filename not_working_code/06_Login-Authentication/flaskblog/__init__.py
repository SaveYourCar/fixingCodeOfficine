from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt # importo la classe Bcrypt dal pacchetto flask-bcrypt installato prima


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) # instanzio bcrypt

from flaskblog import routes # importiamo i routes in basso per evitare importi circolari