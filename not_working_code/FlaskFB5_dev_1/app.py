from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
db = SQLAlchemy(app)
#from models.userModel import User

#Model User
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    confirmPassword = db.Column(db.String(60), nullable=False)
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
        user_var = User(username=name_var, email=email_var, password=password_var, confirmPassword=confirmPassword_var)
        db.session.add(user_var)
        db.session.commit()
    flash("I tuoi dati sono stati salvati!", category='succes_register')
    return redirect(url_for('main'))

@app.route('/login')
def login():
    return render_template('login.html', title='Login')


if __name__ == "__main__":
    app.run(debug=True)