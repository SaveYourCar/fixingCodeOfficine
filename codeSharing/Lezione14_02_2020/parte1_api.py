#Soluzione Esercizio: parte1 - API
from flask import Flask, jsonify, request
from flask_restplus import Api, Resource, fields

#Una volta importate le librerie necessarie istanzio Flask
#Di seguito istanzio l'Api e definisco il mio namespace
app = Flask(__name__)

api = Api(app)

text = api.namespace('api/v1.0/text')

#Definisco un modello che mi aspetterò nell'implementazione della post
#Questa parte non è necessaria 
#ma l'ho fatta per completezza.

textModel = text.model('textModel', {
    'text' : fields.String(required=True, validate=True)
})

#Definisco un endpoint dove implementerò le mie funzioni get e post

@text.route('/')
class GET_Hello(Resource):
    def get(self):
        """ Questa GET restituisce 'Hello World!' """
        return 'Hello World!'

    # Implemento la mia post, richiedendo in entrata il mio modello,
    # Avrei potuto non chiederlo ma comunque restituire 
    # 200 se mi arriva un JSON.
    @text.expect(textModel, validate=True)
    def post(self):
        """Questa POST riceve un JSON contenente un testo sotto la chiave 'text'"""
        r = request.get_json()['text']
        # Recupero dalla richiesta il JSON che mi è stato inviato
        # e salvo il valore contenuto 
        # sotto la chiave text su una variabile r.
        # In reguito ritorno r in formato stringa.
        # In quanto il valore di ritorno deve essere una stringa.
        return str(r)

#Mando in run la mia API in localhost sulla porta 5000 di default

if __name__ == '__main__':
    app.run(debug=True)