"""API base per l'iserimento, il recupero, l'aggiornamento e l'eliminazione
dati in un db sqlite gestito con SQLAlquemy tramite Flask"""

from flask import Flask, jsonify, request, abort
import requests
import json
from flask_restplus import Api, Resource, reqparse, fields
from flask_sqlalchemy import SQLAlchemy

"""Inizializziamo la classe Flask che gestirà e farà partire la nostra app"""

app = Flask(__name__)

"""Inizializziamo la classe Api, presente in flask_restplus,
 che gestirà e darà la struttura alle nostre api.
 Grazie all'integrazione di flask_restuplus con swagger potremo
 inoltre usufruire di un'interfaccia grafica.
 Assegnamo quindi una versione, un titolo e una descrizione
 che potremo visualizzare nella nostra pagina di API"""

api = Api(app, version='1.0', title='Sample Users_Insert API',
    description='API for insert users in a DB')

"""Dichiariamo un namespace per le nostre API.
Questo ci consente di dare un nome alla nostra api (in questo caso users)
e di assegnare una route di base, la quale verrà ereditata da
tutti gli endpoint associati all'api users."""

users = api.namespace('api/v1.0/users',description='CRUD operation for users')

"""Instanziamo e configuriamo la posizione del nostro db sqlite gestito da
SQLAlchemy"""

db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db' 

"""Costruiamo il modello del nostro db.
In questo caso è costituito da una sola tabella users."""

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=True)
    avatar = db.Column(db.String, nullable=True, default='https://shmector.com/_ph/4/184260380.png')
    description = db.Column(db.String, nullable=True)

    """All'interno della classe users definiamo un metodo che
    ci consente di trasformare un'istanza della classe users 
    in un dizionario.
    Così facendo sarà possibile trasformare tale dizionario in un json,
    attraverso la funzione jsonify.
    Questo ci è necessario per dare un valore di ritorno valido 
    alle nostre funzioni GET, POST etc.."""

    def asDict(self):
        return { 'id' : self.id,
                 'name' : self.name,
                 'email' : self.email,
                 'description' : self.description,
                 'avatar' : self.avatar }

"""Creiamo il nostro db che conterrà quindi una tabella user"""

db.create_all()


"""Costruiamo un modello di inserimento dati.
Tale modello dovrà consentire al client di inserire dei dati,
tramite la nostra API, in un valido formato JSON.
Per far ciò utilizziamo il metodo model presente nella classe Api
( quindi nella nostra istanza api, rinominata users ).
Gli diamo in entrata:
- Un nome arbitrario con cui verrà indicato il nostro
    modello di inserimento.
- Un dizionario. Avente come chiavi i nomi delle colonne 
    della nostra tabella user.
    Come valori dei campi vuoti di tipo fields.String().
    Tale tipo definisce, in questo caso, definisce un campo di
    tipo stringa nella compilazione del JSON. Le regole che definisono
    tale campo son definite nella funzione fields 
    della libreria flask_restplus.
"""

userModel = users.model('userModel', {
    'name' : fields.String(),
    'email' : fields.String(),
    'description': fields.String(),
    'avatar' : fields.String()
})


"""Definiamo alcuni parser necessari qualora si voglia richiedere parametri
tramite argomento. Cioè nella forma detta "Query string parameters"
In questo caso una richiesta get sarà ad esempio: 
    api/v1.0/users?user_id=1 
    
In questo caso ho definito un parser non necessario che richiamerò in una GET
e un parser necessario che richiamerò in una DELETE.
Il fatto che sia necessario è garantito dalla linea di codice : nullable=False"""

parserGet = reqparse.RequestParser()
parserGet.add_argument('user_id',type=int)

parserDelete = reqparse.RequestParser()
parserDelete.add_argument('user_id',type=int, nullable=False)


"""Definisco il primo endpoint.
Qui costruiamo 3 chiamate html: GET POST e DELETE.
- Associamo una route all'api users.
- Definiamo una classe dal nome arbitrario che erediterà
    le sue caratteristiche dalla classe Resource presente in
    flask_restplus. 
    Tale classe ci consente di dare a questo endpoint le 
    caratteristiche peculiari di una RESTFUL API.
- All'interno della classe definiamo dei metodi corrispondenti
    alle chiamate html che vogliamo effettuare nel nostro endpoint.
"""

@users.route('/')
class GET_POST_DELETE_Users(Resource):
    """GET: Questa funzione get consente di recuperare uno
    o tutti gli utenti, a seconda della presenza o meno 
    del parametro user_id. 
    La richiesta del parametro opzionale avviene tramite la linea di codice:
    @users.expect(parserGet) 
    dove parserGet corrisponde al parser che abbiamo definito sopra.
    """
    @users.expect(parserGet)
    def get(self):
        if request.args.get('user_id'):
            """Questo if controlla se è presente il parametro user_id.
            Quindi se si è richiesta una get per un singolo user o per 
            tutti gli user nel db.
            L'argomento user_id in questione, qualora presente, viene recuperato
            tramite il metodo flask request. Da cui: request.args.get('user_id').
            Una volta assegnato il valore dell'argomento ad una variabile user_id,
            facciamo una query che controlla la presenza effettiva di quell'id nella
            tabella user.
            Se usernon è presente restituiamo un errore 404.
            In caso sia presente, invece, i dati dell'utente richiesto.
            Una chiamata html deve però restituire necessariamente un JSON
            (o al massimo un xml) perciò dobbiamo prima trasformare i dati
            recuperati dalla query in un json.
            La funzione jsonify non ci consente di trasformare direttamente 
            la query user ma necessita di un formato lui più comprensibile.
            Per questo trasformiamo user in un dizionario grazie al metodo 
            asDict definito sopra nella classe User. Da cui: 
            jsonify(user.asDict()).
            """
            user_id=request.args.get('user_id')
            user = User.query.get_or_404(user_id)
            if not user:
                abort(404)
            return jsonify(user.asDict())
        else:
            """Se invece l'argomento user_id non è presente restituiamo tutti gli utenti.
            Per far questo:
            - inizializziamoun dizionario (users_dict)vuoto che li conterrà.
            - Faciamo la query al db che recupera tutti gli users ordinati per nome
            - Costruiamo un ciclo for che di volta in volta riempie il dizionario users_dict
            con ciascun utente presente in users trasformato a sua volta in dizionario
            grazie al metodo asDict.
            - Diamo al return users_dict trasformato in json tramite jsonify"""
            users_dict = {}
            users = User.query.order_by(User.name).all()
            i=0
            for user in users:
                i+=1
                users_dict[i] = user.asDict()
            return jsonify(users_dict)

    """DELETE: Questa funzione consente di eliminare un utente dal db.
    Per accedervi è necessario inserire un id esistente.
    In risposta, restituisce un json contenente un messaggio 
    di avvenuta eliminazione.
    Per far ciò occorre:
    - Aggiungere il decoratore @users.expect(parserDelete) che richiede
        l'inserimento dell'user_id.
        Tale inserimento sarà contrassegnato come obbligatorio in quanto abbiamo
        Specificato nullable=False nella definizione del parserDelete.
    - Assegnare alla variabile user_id il valore dell'argomento user_id.
    - Fare la query che cerca la presenza dell'user nel db e in caso di successo
        lo assegna alla variabile user.
    - Mettere in stage l'eliminazione dell'utente dal db traminte 
        il metodo session.delete di SQLAlchemy
    - Committare la richiesta di eliminazione con session.commit()
    - restituire una risposta positiva, 
        in caso l'eliminazione sia andata a buon fine, trasformando
        un dizionario contenente un messaggio in json con jsonify"""

    @users.expect(parserDelete)
    def delete(self):
        user_id=request.args.get('user_id')
        user = User.query.get_or_404(user_id)
        if not user:
            abort(404)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'result': True})

    """POST: questa funzione consente di aggiungere un utente al db.
        E caratterizzata dalla richiesta dei parametri tramite json.
        Cioè nella forma detta "Request body parameters".
        - Aggiungiamo il decoratore @users.expect(userModel) 
            Tale decoratore richiederà al client la compilazione di un json
            strutturato come il nostro userModel, che abbiamo costruito sopra
            in modo tale che rispecchi i campi della tabella user del nostro db.
        - Recuperiamo i dati dal json tramite il metodo request.get_json() 
            e li memorizziamo in una varabile data.
        - Scompattiamo i dati recuperando di volta in volta tutti i campi presenti
             e associandoli a delle variabili: user_name, user_avatar etc...
        - Inizializziamo un oggetto della classe user (new_user) i cui attributi
            avranno come valori i dati che abbiamo recuperato dal nostro json.
        - Apriamo una sessione del db e vi committiamo il nostro new_user.
        - Restituiamo un json applicando lafunzione jsonify al dizionario contenente 
            i dati del new_user. """
    @users.expect(userModel)
    def post(self):
        data = request.get_json()
        user_name = data.get('name') 
        user_description = data.get('description')
        user_avatar =  data.get('avatar')
        user_email =  data.get('email')
        new_user = User(
        name=user_name,
        email=user_email,
        avatar=user_avatar,
        description=user_description)
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.asDict())

"""Definisco un secondo endpoint.
Questo endpoint è caratterizzato dalla richiesta di un parametro user_id
tramite la forma "Path parameters".
Cioè questo parametro verrà inviato direttamente nell'url senza '?':
Ad esempio noi server potremo ricevere una chiamata get della forma:
    api/v1.0/users/1

Qui costruiamo 2 chiamate html: GET e PUT.
- Associamo una route all'api users che in questo caso conterrà 
    il tipo e il nome del parametro richiesto.('/<int:user_id>')
- Definiamo una classe dal nome arbitrario che erediterà
    le sue caratteristiche dalla classe Resource presente in
    flask_restplus. 
- All'interno della classe definiamo i metodi corrispondenti
    alle chiamate html che vogliamo effettuare nel nostro endpoint.
"""

    
@users.route('/<int:user_id>')
class GET_PUT_User(Resource):
    """GET: questa funzione ci permette di recuperare un singoloutente dal db.
        A differenza della get definita nel precedente endpoint, questa invia il 
        paramentro nella forma Path.
       - Diamo in entrata alla funzione get il parametro user_id ricevuto nell'url.
       - Facciamo la query al db verificando che l'utente esista.
       - Se esiste restituiamo un json con i dati dell'utente"""
    def get(self,user_id):
        user = User.query.get_or_404(user_id)
        if not user:
            abort(404)
        return jsonify(user.asDict())

    """PUT: questa funzione ci permette di modificare i dati di un utente nel db.
       - Diamo in entrata alla funzione put il parametro user_id ricevuto nell'url.
       - Facciamo la query al db verificando che l'utente esista.
       - Se esiste gli assegnamo il nome user.
       - Recuperiamo i dati dal json richiesto nel body.
       - Assegniamo ai campi dell'tente user i valori dei campi del json,
         se questi non sono vuoti, altrimenti li lasciamo invariati.
       - Committiamo i cambiamenti effettuati.
       - Restituiamoi json contenente i dati dell'utente."""

    @users.expect(userModel)
    def put(self,user_id):
        user = User.query.get_or_404(user_id)
        if not user:
            abort(404)
        data = request.get_json()
        user.name = data.get('name') if data.get('name') else user.name
        user.description = data.get('description') if data.get('description') else user.description
        user.avatar =  data.get('avatar') if data.get('avatar') else user.avatar
        user.email =  data.get('email') if data.get('email') else user.email
        db.session.commit()
        return jsonify(user.asDict())

"""Lanciamo il nostro servizio REST API"""

if __name__ == '__main__':
    app.run(debug=True)
