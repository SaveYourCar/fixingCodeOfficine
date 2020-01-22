document.addEventListener('DOMContentLoaded', function(){/*la function è la callback*/

  //DEVO FARE LA GET

  get(
    "https://reqres.in/api/users/1", //URL
  
    function(request) { // Success Callback
      var response =
        request.currentTarget.response || request.target.responseText;
      console.log("get result", response);
      //ADESSO GENERO LE CARD CON QUESTO JSON
      /*var personaText = '{"id":"titolo", "nome":"Filippo", "cognome":"Basciu", "descrizione":"forza Cagliari", "Img_URL":"https://images.unsplash.com/photo-1577993625454-1dec02cedd4b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60"}';
      console.log("stampo la stringa personaText", personaText)*/
  
      var userArray = JSON.parse(response).data;
      console.log("Stampo l'oggetto convertito dalla stringa", userArray);


      

      var p = document.getElementById("card-container");
    /*console.log(a[0].style);
    var p = a[0].parentNote;
    console.log(p);*/

    for (let i = 0; i < userArray.length; i++) {
      var id = userArray[i].id
      var titolo = userArray[i].first_name + ' ' +userArray[i].last_name;
      var descrizione = userArray[i].email;
      var Img_URL = userArray[i].avatar; 
        p.innerHTML +='<div class="card col-xs-12 col-sm-12 col-md-6 col-lg-4">'+
        '<img class="avatar" src="'+ Img_URL +'"/>'+
        '<h2>'+ titolo +'</h2>'+
        '<p>'+ descrizione +'</p>'+
        '<p><a class="btn btn-secondary" href=/api/user/' + id +' role="button">View details &raquo;</a></p>'+
      '</div>';
    }

  


    },
    /*errorHandler //ERROR CALLBACK*/
    function(){
      var p = document.getElementById("card-container");
      p.innerHTML = "";
      p.innerHTML = '<div class="alert alert-danger col-sm-12"> Errore di caricamento dati.</div>'
    }
  );
    
    
   /* var persona = {
       nome: 'Filippo',
       cognome: 'Basciu',
       età: 45,
       altezza: 176  
    };*/
    /*console.log("Stampo l'istanza dei persona", persona);*/


    /*var personaText = '{"nome":"Filippo", "cognome":"Basciu", "età":"45", "altezza":"176"}';*/
   


    /*var jsonFromString = JSON.parse(personaText);
    console.log("Stampo l'oggetto convertito dalla stringa", jsonFromString);*/

   /* var jsonFromString = JSON.stringify(jsonFromString);
    console.log("Stampo il json text convertito dall'oggetto", jsonFromString);*/




    
    
  });


 

