from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from flask_mysqldb import MySQL
from data import Articles
from wtforms import Form, StringField , TextAreaField ,PasswordField , validators
from wtforms.validators import DataRequired, Length, Email, EqualTo
from passlib.hash import sha256_crypt

app = Flask(__name__)

#collegamento Database
#Config MySQL
app.config['SECRET_KEY'] = '12wfregrgrthytrytryr45'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'myflaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
#init MYSQL
mysql = MySQL(app)


Articles=Articles()


@app.route('/')
def index():
    return render_template('home.html', title='Home')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/articles')
def articles():
    return render_template('articles.html', articles=Articles, title='Articles')

@app.route('/article/<string:id>')
def article(id):
    # Con questo for cerco quale dei dizionari in Articles
    # ha come chiave id, quella passata nell'url.
    # Trovato il giusto elemento, lo invio per intero al template.
    # In questo modo posso accedere, dal template, ad ogniuna delle sue chiavi.
    # ( id, title, body, etc..)
    for item in Articles:
        print(item['id'],item['id'] == id)
        if item['id'] == int(id):
            return render_template('article.html', article=item, title=item['title'])

class RegisterForm(Form):
        name = StringField('Name',[validators.Length(min=1,max=50)])
        username = StringField('Username',[validators.Length(min=4,max=25)])
        email = StringField('Email',[validators.Length(min=4,max=25)])
        password = PasswordField('Password', [validators.DataRequired(),
                    validators.EqualTo('confirm',message ='passwords do not match')])
        confirm = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])

@app.route('/register', methods=['GET','POST'])
def register():
        form = RegisterForm(request.form)
        if request.method == 'POST' and form.validate():
            name = form.name.data
            email = form.email.data
            username = form.username.data
            password = sha256_crypt.encrypt(str(form.password.data))
            
            # Create crusor
            cur = mysql.connection.cursor()
            cur.execute("INSERT INTO users(name,email,username,password) VALUES(%s,%s,%s,%s,%s)", [name,email,username,password])

            # commit to DB
            mysql.connection.commit()
            #close connection
            cur.close()
            flash("You are now Registerd and you can login", 'success')
            redirect(url_for('index'))
                        
            return render_template('home.html')
        return render_template('register.html',form=form, title='Register')

if __name__=='__main__':
    app.run(debug=True)
    