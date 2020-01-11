# installazione flask-sqlalchemy
pip install flask-sqlalchemy

# importare SQLAchemy su flaskblog.py
from flask_sqlalchemy import SQLAlchemy

# specificare URI database dove è posizionato
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# istanza del database
db = SQLAlchemy(app)

# creazione della class User per i dati utente
-inserire la relazione uno a molti con la class post
 posts = db.relationship('Post', backref='author', lazy=True)

# creazione della  auto-variabile con metodo repr

# creazione della class Post
-per inserire la data del post si importa:
from datetime import datetime
-specificare l'utente di uno specifico post
-set della foreignKey per specificare l'autore del post specifico:
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

date_posted = db.Column(db.Datetime, nullable=False, default=datetime.utcnow)

#per creare il database da riga di comando con python
-digitare python + invio
-from flaskblog import db + invio
-db.create_all()
<si deve creare un file site.db nella directory principale>
-importare i models User e Post con
    from flaskblog import User, Post

#aggiungere dati al DB
esempio user_1 user_2
>>> from flaskblog import db
>>> db.create_all() <dopo questo comando si crea il db site.db nella main folder>
>>> from flaskblog import User, Post
>>> user_1 = User(username='Marco', email='marco@demo.com', password='ciao2')  
>>> db.session.add(user_1)
>>> user_2 = User(username='Luigi', email='luigi@demo.com', password='ciao3') 
>>> db.session.add(user_2) 
>>> db.session.commit()
>>> 



db.session.add(user_1) <predispone i dati per essere aggiunti>

db.session.commit() <invia i dati al database>

#per fare una queri del DB
User.query.all()

