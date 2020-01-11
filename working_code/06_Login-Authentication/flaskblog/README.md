# login and authentication

<per hashare le password usiamo flask-bcrypt>
-dentro la venv
pip install flask-bcrypt

-su __init__.py importo:
from flask_bcrypt import Bcrypt

-instanziare bcrypt come variabile

-su routes.py importare db e bcrypt
from flaskblog import app, db, bcrypt

#creiamo il db da riga di comando
>>> from flaskblog import db

>>> from flaskblog.models import User
>>> user = User.query.first()
>>> user
>>> User
>>> db.create_all() <dopo questo si crea il db>
>>> User.query.all() <con questa query vediamo che la tabella User è vuota>

