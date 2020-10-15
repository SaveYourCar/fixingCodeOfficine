from flask import Flask, render_template
from data import Articles

app = Flask(__name__)

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
    return render_template('article.html', id=id, title='Article One')




if __name__=='__main__':
    app.run(debug=True)
    