from flask import Flask, request, jsonify
from flask_restplus import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
api = Api(app,
        version= '0.1',
        title='The other api',
        description='endpoints product project ',
        endpoint='api')

product = api.namespace('product', description = 'CRUD operation for product')
#riga sotto localizza correttamente i file del db grazie alla path che lo indirizza a os
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
#riga sotto non serve ma se non lo inseriamo da qualche problem alla ricerca del db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#riga sotto init db e lo passiamo nella nostra app
db = SQLAlchemy(app)
#init Marshmallow e la passiamo nella nostra app
ma = Marshmallow(app)

#product class/name/model creiamo una classe prodotto e la faccciamo passare nel nostr db
class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
  description = db.Column(db.String(200))
  price = db.Column(db.Float)
  qty = db.Column(db.Integer) #qty = quantità

  #def __repr__(self):
     #return f"Product('{self.name}', '{self.description}', '{self.price}', '{self.qty}')"

#riga sotto inizializziamo il costruttore
  def __init__(self, name, description, price, qty):
    self.name = name #passiamo l'istanza (nome etc) della classe product attraverso la funzione sopra (richiamandola sotto con self)
    self.description = description
    self.price = price
    self.qty = qty

#sotto diamo il commando per creare il nostro db e lanciamo
#  in run (app) da terminale per effettuare la creazione
db.create_all()

#stiamo creando uno classe/schema di prodotti che passiamo a marshmallow
class ProductSchema(ma.Schema):
#la sotto clssse meta ci permette attraverso una richiesta get di mostrare
#    i prodotti con i propri attributi
  class Meta:
    fields = ('id', 'name', 'description', 'price', 'qty')

    #def decorator_function(original_function):
    #    def wrapper_function(*args, **kwargs):
    #        return wrapper_function

# Init schema
product_schema = ProductSchema()
#lo schema (la classe sopra) del prodotto passa (un solo prodotto per volta)
#    dentro il metodo strict che ho cancellato perchè da problemi
products_schema = ProductSchema(many=True)
#lo schema (la classe sopra) passa più  prodotti attraverso many dentro il metodo strict (come sopra delete problems)

# Create a Product
@app.route('/product', methods=['POST'])  #endpoint (percorso del prodotto)
def add_product(): #attraverso questa funzione facciamo la chiamata per aggiungere un prodotto
  name = request.json['name'] #variabile che attraverso la richiesta_json recuperano e ci rende i dati in json
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

#introduciamo i dati passati da post
  new_product = Product(name, description, price, qty)

  db.session.add(new_product)
  db.session.commit() #salva nel db il nuovo prodotto aggiunto
                      #attraverso post e la classe Product grazie alla variabile new_product
                      #che viene chiamata in db session add

  return product_schema.jsonify(new_product)#ci rende i dati in json di un solo prodotto aggiunto

# Get All Products
@app.route('/product', methods=['GET'])
def get_products():
  all_products = Product.query.all() #metodo query
  result = products_schema.dump(all_products) #dump scrarica schema di tutti i prodotti
  return jsonify(result.data) #da come risultato un dixionario di dati

# Get Single Products
@app.route('/product/<id>', methods=['GET'])
def get_product(id):
  product = Product.query.get(id)
  return product_schema.jsonify(product)

# Update a Product
@app.route('/product/<id>', methods=['PUT'])
def update_product(id):
  product = Product.query.get(id)
  name = request.json['name']
  description = request.json['description']
  price = request.json['price']
  qty = request.json['qty']

  product.name = name
  product.description = description
  product.price = price
  product.qty = qty

  db.session.commit()

  return product_schema.jsonify(product)

# Delete Product
@app.route('/product/<id>', methods=['DELETE'])
def delete_product(id):
  product = Product.query.get(id)
  db.session.delete(product)
  db.session.commit()

  return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
