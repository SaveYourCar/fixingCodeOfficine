from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import ( UserMixin, current_user, logout_user,
                        login_user, LoginManager )

app = Flask(__name__)

app.config["SECRET_KEY"] = 'weeekrtkssfsfdfjd98434673'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)
#from models.userModel import User

#E necessario inizializzare un oggetto LoginManager
#per gestire le sessioni utente
login = LoginManager(app)


#Decoratore necessario all'utilizzo di flask-LoginManager
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

#Model User

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

db.create_all()

@app.route("/")
@app.route("/main")
def main():
    return render_template("home.html", title='Home')

@app.route('/showSignUp', methods=['GET','POST'])
def showSignUp():
    if request.method=='GET':
        return render_template('signup.html', title='Sign Up')
    elif request.method=='POST':
        dati = request.form
        name_var = dati['inputName']
        email_var = dati['inputEmail']
        password_var = dati['inputPassword']
        confirmPassword_var=dati['inputConfirmPassword']
        if password_var == confirmPassword_var:
            user_var = User(username=name_var, email=email_var, password=password_var)
            db.session.add(user_var)
            db.session.commit()
            flash("I tuoi dati sono stati salvati!", category="succes_register")
        else:
            flash("Le password non coincidono. Per piacere reinserisci i dati corretti!", category="txt1")
            return render_template('signup.html', title='Sign Up')
    return redirect(url_for('main'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main'))
    elif request.method=='POST':
        dati = request.form
        name_var = dati['username']
        password_var = dati['pass']
        user = User.query.filter_by(username=name_var).first()
        if not user or password_var != user.password:
            flash('username o password non corretti', category="txt1")
            return redirect(url_for('login'))
        login_user(user)
        flash("Login avvenuto con successo!", category="succes_register")
        return redirect(url_for('main'))
    return render_template('login.html', title='Login')

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main'))

if __name__ == "__main__":
    app.run(debug=True)