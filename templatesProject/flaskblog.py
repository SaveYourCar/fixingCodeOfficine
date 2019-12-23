from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        " autore " : " Corey Schafer " ,
        " title " : " Blog Post 1 " ,
        " contenuto " : " contenuto del primo post " ,
        "Date_posted" : "20 Aprile 2018 " 
    },
    {
        " autore " : " Jane Doe " ,
        " title " : " Blog Post 2 " ,
        " contenuto " : " contenuto del secondo post " ,
        "Date_posted"   : " 21 aprile 2018"
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',title='Home', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)
