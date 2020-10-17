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
    # Con questo for cerco quale dei dizionari in Articles
    # ha come chiave id, quella passata nell'url.
    # Trovato il giusto elemento, lo invio per intero al template.
    # In questo modo posso accedere, dal template, ad ogniuna delle sue chiavi.
    # ( id, title, body, etc..)
    for item in Articles:
        print(item['id'],id,item['id'] == id)
        if item['id'] == int(id):
            return render_template('article.html', article=item)




if __name__=='__main__':
    app.run(debug=True)
    