from flask import Flask, render_template
app = Flask(__name__)

@app.route("/result") # nel browser nell'url dopo il localhost posso scrivere una stringa /result
def result(): # la funzione mi manipola la stringa scritta sull'url
   dict = {'fisica':50, 'chimica':60, 'matematica':70} # dati raccolti nel dizionario
   return render_template("result.html", result = dict) # i valori del dizionario vengono passati alla pag result.html

if __name__ == '__main__':
   app.run(debug = True)

# dopo che eseguo il programma, 
# inserire dopo il localhost la stringa che poi mi 
# viene restituita con stampa a video