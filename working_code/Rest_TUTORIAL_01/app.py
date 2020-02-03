# -------------------------#
"""
N.B.
  - Ho inserito tutti i miei commenti tra # ----- # per distinguerli dai tuoi.
  - Un errore che hai fatto in tuttoil codice è la definizione delle route.
     Se hai istanziato l'api di flask_respluse e l'hai chiamata api, le route le
     devi definire con: @api.route('/...')
  - Non hai mai definito le classi negli endpoint pur avendo utilizzato
    flask_restplus e avendo importato Resource.
    Soppongo che volessi utilizzare swagger.
    Per farlo hai bisogno di:
    - Definire delle classi figlie di Resource.
    - Definire dei metodi col nome o get o post o delete o put.
    - Passare il parametro self che indica l'appartenenza del metodo alla classe
       e ne eredita gli attributi.
    - Definire un modello json da chiedere tramite il decoratore @api.expect(nome_modello)
      O, in alternativa, definire dei parser.
      ( Qui ti ho corretto il codiceusando il modello ma puoi trovare esempi di parser
        nei miei codici )
"""
# -------------------------#

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
# -------------------------#
#Queste linee di codice non servono
#basedir = os.path.abspath(os.path.dirname(__file__))
# Database
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
# -------------------------#
#Basta questa per specificare che vuoi il db nella stessa cartella dove lo stai definendo
#P.S. Se le vuoi tenere non importa. Puoi vedere il codice che ho corretto a filippo
# dove gliele lascio.
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# -------------------------#
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
# -------------------------#
#Se vuoi avere i metodia a dispozizione nell'interfaccia swagger
#Devi definirli come funzioni post, get etc.. sotto delle classi
#Che ereditano dalla classe di flask_restplus Resource.
#Inoltre è neccessaria una richiesta di agomenti.
#Cosa che usando curl o postman non è necessaria
#In quanto è a discrezione tua inserirli o meno.
#Perciò occorre definire:
# - o dei parser
#   (Che consentono di richiedere i parametri col metodo Query).
# - o un modello json
#   (Che consentono di richiedere i parametri col metodo Path) 
# -------------------------#
# Modello JSON per Path Parameters:
productModel = api.model('productModel', {
    'name' : fields.String(),
    'description': fields.String(),
    'price' : fields.Float(),
    'qty' : fields.Integer()
})
# -------------------------#
@api.route('/product', methods=['POST'])  #endpoint (percorso del prodotto)
class Add_Product(Resource):
  @api.expect(productModel)
  def post(self): #attraverso questa funzione facciamo la chiamata per aggiungere un prodotto
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
# -------------------------#
# Non è necessario definire un diverso endpoint per ongni chiamta html
# Ma se lo vuoi fare devi effettivamente distinguerli.
# Due endpoint non possono avere la stessa route '/product'
# In questo caso ti ho modificato la seconda route in product_get
# Ma non è unmetodo consono a definire endpoint per API
# Dovresti definire tutte le chiamate possibili utilizzando
# Un endpoint della forma : /api/v1.0/products
# Possibilmente definendolo nel namespace.
# -------------------------#
@api.route('/product_get', methods=['GET'])
class Get_Products(Resource):
  def get(self):
    all_products = Product.query.all() #metodo query
    # -------------------------#
    #Questoè un metodo relativo a marshmallow SQLALchemy ModelSchema
    #Non a Marshmallow Schema.
    #result = products_schema.dump(all_products) #dump scrarica schema di tutti i prodotti
    #In questo caso ti basta fare così:
    return products_schema.jsonify(all_products) #da come risultato un dixionario di dati
    # -------------------------#


# Get Single Products
 # -------------------------#
# Questa chiamata richiede il parametro in Path
# Va bene ma dovresti specificare il tipo nel path
# Es: <int:product_id>
# Ti ho comunque lasciato l'endpoint come lo hai scritto te
# Perchè comunque, con ledovute correzioni, funziona.
 # -------------------------#
@api.route('/product/<id>', methods=['GET'])
class Get_Products(Resource):
  def get(self,id):
    product = Product.query.get(id)
    return product_schema.jsonify(product)

# Update a Product
 # -------------------------#
# Questa PUT funziona ma in pratica cancella tutti i vecchi dati,
# almeno che non li riscriva uguali nel JSON.
# In modo tale che faccia proprio l'update devi inserire degli if.
# Qesti devono controllare se si sono inseriti degli aggiornamenti
# o meno. In caso non si siano inseriti gli aggiornamenti e il campo 
# JSON figura vuoto( cioè così: "" ) allora i dati devo restare 
# quelli vecchi.
# Prova a fare te questa modifica.
# -------------------------#
@api.route('/product_get/<id>', methods=['PUT'])
class Update_Product(Resource):
  @api.expect(productModel)
  def put(self,id):
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
# -------------------------#
# Va bene ma è meglio che ritorni un json 
# di avvenuta eliminazione anzihè il prodotto che
# è stato eliminato.
# -------------------------#
@api.route('/product_delete/<id>', methods=['DELETE'])
class Delete_Product(Resource):
  def delete(self,id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()

    return product_schema.jsonify(product)

# Run Server
if __name__ == '__main__':
  app.run(debug=True)
