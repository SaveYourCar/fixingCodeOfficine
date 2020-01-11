import os
from PIL import Image
from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db
from flaskblog.forms import PostForm, SearchForm
from flaskblog.models import Post
from sqlalchemy import desc
import string



@app.route("/")
@app.route("/home")
def home():
    #lista = list(string.ascii_lowercase)
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).order_by(Post.nome).paginate(page=page, per_page=20)
    return render_template('home.html', posts=posts)

@app.route("/NomiFemminili")
def NomiFemminili():
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).filter_by(genere=True).order_by(Post.nome).paginate(page=page, per_page=10)
    return render_template('nomifemminili.html', posts=posts)

@app.route("/NomiMaschili")
def NomiMaschili():
    page = request.args.get('page', 1, type=int)
    posts = db.session.query(Post).filter_by(genere=False).order_by(Post.nome).paginate(page=page, per_page=10)
    return render_template('nomimaschili.html', posts=posts)

@app.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.femminile.data and not form.maschile.data:
            post = Post(nome=form.nome.data.lower().capitalize(), genere=True) 
            db.session.add(post)
            db.session.commit()
            flash('Il tuo nome è stato inserito!', 'success')
            return redirect(url_for('home'))
        elif form.maschile.data and not form.femminile.data:
            post = Post(nome=form.nome.data.lower().capitalize(), genere=False) 
            db.session.add(post)
            db.session.commit()
            flash('Il tuo nome è stato inserito!', 'success')
            return redirect(url_for('home'))
        elif not form.femminile.data and not form.maschile.data:
            flash(u'Devi inserire il genere', 'danger')
        elif form.femminile.data and form.maschile.data:
            flash(u'Devi inserire uno e un solo genere', 'danger')
    return render_template('create_post.html', title='Nuovo Nome',
                           form=form, legend='Nuovo Nome')


@app.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title='Nome', post=post)


@app.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
def update_post(post_id):
    post = Post.query.get(post_id)
    form = PostForm()
    if form.validate_on_submit():
        if form.femminile.data == True:
            post.nome = form.nome.data.lower().capitalize()
            post.genere = form.femminile.data
        elif form.maschile.data == True:
            post.nome = form.nome.data.lower().capitalize()
            post.genere = not form.maschile.data
        else:
            flash('Devi inserire il genere!', 'failure')
        db.session.commit()
        flash('Il nome è stato aggiornato!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.femminile.data = True if post.genere==True else False
        form.maschile.data = True if post.genere==False else False
        form.nome.data = post.nome
    return render_template('create_post.html', title='Update',
                           form=form, legend='Update')


@app.route("/post/<int:post_id>/delete", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Il nome è stato rimosso dal dizionario !', 'success')
    return redirect(url_for('home'))


@app.route("/post/search", methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        if form.femminile.data == True and form.maschile.data == False:
            post = db.session.query(Post).filter_by(nome=form.nome.data.lower().capitalize(), genere=True).first()
            if post:
                flash('Il nome è presente !', 'success')
                return redirect(url_for('post', post_id=post.id))
        elif form.maschile.data == True and form.femminile.data == False:
            post = db.session.query(Post).filter_by(nome=form.nome.data.lower().capitalize(), genere=False).first()
            if post:
                flash('Il nome è presente !', 'success')
                return redirect(url_for('post', post_id=post.id))
        elif form.femminile.data == False and form.maschile.data == False:
            flash(u'Devi inserire il genere', 'danger')
        elif form.femminile.data == True and form.maschile.data == True:
            flash(u'Devi inserire uno e un solo genere', 'danger')
    return render_template('search.html', title='Cerca Nome',
                           form=form, legend='Cerca Nome')

@app.route("/post/selection/<string:alph>/<string:genere>")
def selection(alph,genere):
    session.query(SomeTable).filter(SomeTable.some_column.ilike('{0}%',alph)).all()
    post = db.session.query(Post).filter_by(nome=form.nome.data.ilike('{0}%',alph), genere=True if genere==femminile else False).all()
    return render_template('selection.html', title='alph', post=post)

