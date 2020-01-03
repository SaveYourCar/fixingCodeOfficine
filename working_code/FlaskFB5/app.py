from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

# Configuro un chiave segreta che 
# è necessaria per gestire le sessioni utente e per la
# compilazione e validazione di form
app.config["SECRET_KEY"] = 'weeekrtkssfsfdfjd98434673'
#Configurazione del tipo e della locazione del db
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///site.db'
#Istanza della classe SQLAlchemy, questa gestirà il db.
db = SQLAlchemy(app)


#Model User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

#Una volta costruito il model si può creare il db
db.create_all()


#Controllers
@app.route("/")
@app.route("/main")
def main():
    return render_template("home.html")

@app.route('/showSignUp', methods=['GET','POST'])
def showSignUp():
    if request.method=="GET":
        return render_template('signup.html') 
    elif request.method=="POST":   
        dati = request.form 
        name = dati['inputName']
        email = dati['inputEmail']
        password = dati['inputPassword']
        user =User(name=name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
    flash("I tuoi dati sono stati salvati!", category='succes_register')
    return redirect(url_for('main'))

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == "__main__":
    app.run(debug=True)