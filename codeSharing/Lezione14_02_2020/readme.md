# Esercizio Lezione 14_02_2020

# App flask che comunicano fra loro:

Creare due semplici app flask distinte.
In una delle due implementare un'API, 
in cui sia possibile effettuare una chiamata get e una post.
L'altra app dovrà comunicare con l'API effettuando una chiamata get e una post.

# Suggerimenti:
    - Usare due differenti numeri di porta in modo da poter far girare entrambe le app in localhost.
    - Per effetuare le chiamate all'url dell'API importare la libreria requests di python.

# N.B. 
    Non è necessario usare un db.
    L'importante è che le chiamate vadino a buon fine.
    L'esercizio è considerato ultimato anche se le  risposte a video sono dei semplici Hello World o comunque se il codice di risposta get e post in console è 200.


# Soluzione:

    - Aprire due terminali distinti. (Non entrambi in vs-code)
    - Posizionarsi nella cartellaLezione14_02_2020 in entrambi e attivare
    un virtual-environmant con i requirements installati.
    - Lanciare in uno parte1_api.py e nell'altro parte2_app.py
    - Aprire tre pagine del browser:
        - http://localhost:5000/
        - http://localhost:8000/get_hello
        - http://localhost:8000/post_text
    - Leggere il codice e verificare che il risultato 
    sia quello atteso.


