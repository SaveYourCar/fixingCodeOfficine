#Soluzione Esercizio: parte2 - App di Comunicazione
from flask import Flask
#Importo la libreria requests che mi consente 
# di effettuare chiamate html
import requests
import json

#In questo caso mi serve istanziare solo flask
app = Flask(__name__)

#Definisco una route a cui associo un url dove
#andrò, tramite la funzione get_hello, a chiamare la get.
@app.route('/get_hello',methods = ['GET'])
def get_hello():
    #Tramite il metodo get di requests chiamo l'url della mia API
    r = requests.get('http://localhost:5000/api/v1.0/text/')
    #Essendo la risposta che ottengo di tipo 'Response',
    #Devo utilizzare il metodo json per tradurla in qualcosa
    #Accettabile in ritorno
    return r.json()

#Definisco un'altra route a cui associo un url dove
#andrò, tramite la funzione post_hello, a chiamare la post.
@app.route('/post_text',methods = ['GET','POST'])
def post_text():
    #Tramite il metodo post di requests chimamo l'url dell'API e 
    #Vi mando un JSON conforme alle richieste
    r = requests.post('http://localhost:5000/api/v1.0/text/', json={"text": "All Around The World "})
    #Restituisco a video la risposta dell'API
    return r.json()

#Mando in run l'app sulla porta 8000

if __name__ == '__main__':
    app.run(debug=True, port=8000)