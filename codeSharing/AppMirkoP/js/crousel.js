/*Lezione 27/01/2020 
N.B. 1 - I commenti sono da leggere da quello più in basso a quello più in alto.
     2 - Le funzioni get, remove e put sono definite in ajax.js.
     3 - Per inserire i pulsanti che ci serivano abbiamo scaricato 
          la cartella font da https://fontawesome.com/v4.7.0/assets/font-awesome-4.7.0.zip 

/* Questa funzione serve a far funzionare il pulsante submit
  associato al form dell'updateUser.
  Il suo scopo è chiamre la funzione put.
  Questa è un'operazione che non abbiamo terminato a lezione.
  Vedremo domani la soluzione.
*/

function putCall(id){
  var formdata = document.getElementById("form");
  const apiData = { email: formdata.email.value, first_name: formdata.first_name.value, last_name: formdata.last_name.value };
  var json = JSON.stringify(apiData);
  console.log(json);
  
  put('https://reqres.in/api/users/'+id,
    json,
    function(){console.log('ok')},
    function(){console.log('ko')}
    )
}

/* Questa funzione serve a far funzionare il pulsante 
  associato all'evento closeUpdate.
  Vedi funzionamento closeDetails.
*/

function closeUpdate(id){
  var card = document.getElementById("user_"+id);
  card.getElementsByClassName("intro")[0].style.display="block";
  card.getElementsByClassName("update")[0].remove();
}

/* Questa funzione serve a far funzionare il  pulsante 
  associato all'evento updateUser.
  Per farlo chiama una funzione get che recupera 
  i dati dell'utente col relativo id.
  In caso di successo entra in gioco una funzione succesCallback.
  Questa cambia il contenuto della relativa card user.
  Questo è possibile modificando lo stile 
  della div "intro" e ponendo: display="none".
  Successivamente è necessario ripopolare il contenuto
  della card con una nuova div.
  Quest'ultima sarà  popolata del nuovo contenuto, 
  il quale, in questo caso, è costituito da un form.
  In caso di insuccesso verrà chiamata la errorCallback. 
  In questo caso costituita da
  un semplice console.log.*/
function updateUser(id){
  get(
    "https://reqres.in/api/users/"+id,
    function(request){
          var response =
            request.currentTarget.response || request.target.responseText;
          var user = JSON.parse(response).data;
          var card = document.getElementById("user_"+id);
          card.getElementsByClassName("intro")[0].style.display="none";
          card.innerHTML+='<div class="update">\
              <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 140x140">\
              <image x="0" y="0" width="140" height="140" style="display: block; width: 100%; height: 100%; object-fit: cover;" xlink:href="'+user.avatar+'"/></svg>\
              <form id="form" onsubmit="putCall('+id+')">\
              <div class="form-group">\
                <label for="email">Email address</label>\
                <input name="email" type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Enter email">\
                <small id="emailHelp" class="form-text text-muted">We ll never share your email with anyone else.</small>\
              </div>\
              <div class="form-group">\
                  <label for="first_name">Fisrt Name</label>\
                <input name="first_name" type="text" class="form-control" id="first_name" placeholder="First Name">\
              </div>\
              <div class="form-group">\
                <label for="last_name">Last Name</label>\
                <input name="last_name" type="text" class="form-control" id="last_name" placeholder="Last Name">\
              </div>\
              <button type="submit" class="btn btn-primary">Submit</button>\
              </form>\
              <p><a onclick="closeUpdate('+id+')" class="btn btn-primary col-lg-4 col-xs-4 col-md-4 col-sm-4" href="javascript:void(0)" role="button"><i class="fa fa-window-close-o" aria-hidden="true"></i></a>\
              </p>\
              </div>';
    },
    function(){console.log("ko");}
  )
}

/* Questa funzione serve a far funzionare il  pulsante 
  associato all'evento deleteUser.
  Per farlo chiama la funzione remove.
  In caso di successo entra in gioco una funzione succesCallback.
  La quale elimina la relativa card user.
  In caso di insuccesso verrà chiamata la errorCallback. 
  In questo caso verrà mostrata una div con stile alert-danger.*/

function deleteUser(id){
  remove(
    "https://reqres.in/api/users/"+id,
    function(){
      var card = document.getElementById("user_"+id);
      card.remove();
    },
    function(){
      var p = document.getElementById("card-container");
      p.innerHTML = "";
      p.innerHTML='<div  class="alert alert-danger col-xs-12 col-lg-12">Errore di caricamento dati</div>';
  }
  )

}

/* Questa funzione serve a far funzionare il pulsante 
  associato all'evento closeDetails.
  Quando è stato chimato l'evento userDetails, 
  è possibile tornare alla visualizzazione precedente
  della card cliccando su un'icona a forma di x.
  Per far ciò basta recuperare la card in questione tramite il metodo:
  getElementById.
  Successivamente è necessario porre lo stile dell div "intro" 
  (che racchiude il contenuto) su display="block".
  Infine occorre rimuovere la div "details" che conteneva i dettagli
  inseriti nella funzione userDetails.
  */
function closeDetails(id){
  var card = document.getElementById("user_"+id);
  card.getElementsByClassName("intro")[0].style.display="block";
  card.getElementsByClassName("details")[0].remove();
}


/* Questa funzione serve a far funzionare il  pulsante 
  associato all'evento userDetails.
  Per farlo chiama una funzione get che recupera 
  i dati dell'utente col relativo id.
  In caso di successo entra in gioco una funzione succesCallback,
  la quale cambia il contenuto della relativa card user.
  Questo è possibile modificando lo stile 
  della div "intro" e ponendo: display="none".
  Successivamente è necessario ripopolare il contenuto
  della card con una nuova div.
  Quest'ultima sarà  popolata del nuovo contenuto.
  In caso di insuccesso verrà chiamata la errorCallback. 
  In questo caso costituita da
  un semplice console.log.*/
function userDetails(id){
  get(
    "https://reqres.in/api/users/"+id,
    function(request){
          console.log("ok");
          var response =
            request.currentTarget.response || request.target.responseText;
          var user = JSON.parse(response).data;
          console.log("get result:", user);
          var card = document.getElementById("user_"+id);
          card.getElementsByClassName("intro")[0].style.display="none";
          card.innerHTML+='<div class="details">\
              <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 140x140">\
              <image x="0" y="0" width="140" height="140" style="display: block; width: 100%; height: 100%; object-fit: cover;" xlink:href="'+user.avatar+'"/></svg>\
              <h2>'+user.first_name+'</h2>\
              <h2>'+user.last_name+'</h2>\
              <p><a onclick="closeDetails('+id+')" class="btn btn-primary col-lg-4 col-xs-4 col-md-4 col-sm-4" href="javascript:void(0)" role="button"><i class="fa fa-window-close-o" aria-hidden="true"></i></a>\
              </p>\
              </div>';
    },
    function(){console.log("ko");}
  )
}

/*Questa è la funzione che faceva visualizzare la lista degli utenti.
Abbiamo iniziato inserendo dei pulsanti sulla parte bassa delle card.
Details, Update, Delete.
Successivamente abbiamo associato a tali pulsanti degli eventi: onclick.
Per ogni evento abbiamo definito una funzione che determinava il comportamento
di tali pulsanti.*/
document.addEventListener('DOMContentLoaded',function(){
  
  get(
        "https://reqres.in/api/users?page=1&per_page=30",
        function(request) {
          var response =
            request.currentTarget.response || request.target.responseText;
          var user = JSON.parse(response).data;
          console.log(JSON.parse(response).data)
          var container = document.getElementById("cards-container");
          container.innerHTML = '';
          for(let i=0; i<user.length;i++){
              container.innerHTML+='<div id="user_'+user[i].id+'" class="col-lg-4 col-xs-12 col-md-12 col-sm-12">\
              <div class="intro">\
              <svg class="bd-placeholder-img rounded-circle" width="140" height="140" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: 140x140">\
              <image x="0" y="0" width="140" height="140" style="display: block; width: 100%; height: 100%; object-fit: cover;" xlink:href="'+user[i].avatar+'"/></svg>\
              <h2>'+user[i].first_name+'</h2>\
              <p>'+user[i].email+'</p>\
              <p><a onclick="userDetails('+user[i].id+')" class="btn btn-success col-lg-2 col-xs-1 col-md-1 col-sm-1" href="javascript:void(0)" role="button"><i class="fa fa-eye" aria-hidden="true"></i></a>\
              <a onclick="updateUser('+user[i].id+')" class="btn btn-primary col-lg-2 col-xs-1 col-md-1 col-sm-1" href="javascript:void(0)" role="button"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></a>\
              <a onclick="deleteUser('+user[i].id+')" class="btn btn-danger col-lg-2 col-xs-1 col-md-1 col-sm-1" href="javascript:void(0)" role="button"><i class="fa fa-trash-o" aria-hidden="true"></i></a>\
              </p>\
              </div>\
              </div>';
          }
        },
        function(){
            var p = document.getElementById("card-container");
            p.innerHTML = "";
            p.innerHTML='<div  class="alert alert-danger col-xs-12 col-lg-12">Errore di caricamento dati</div>';
        }
      );
});