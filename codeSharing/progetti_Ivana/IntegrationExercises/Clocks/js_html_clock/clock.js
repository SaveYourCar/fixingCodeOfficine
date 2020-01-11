var sheet = document.createElement('style')
sheet.innerHTML = "\
body {\
    background-image: url('fixedbg.jpg');\
    background-repeat: no-repeat;\
    background-attachment: fixed;\
  }\
table {    \
    background-image: inherit;\
    background-repeat: no-repeat;\
    background-attachment: fixed;\
    width: 100%;\
    height: 100%;\
    text-align: center;\
    }\
td {\
    vertical-align: middle;\
    color: bisque;\
    font-family: 'Lucida Sans';\
    font-size: 20.25em;\
    text-shadow: 25px 22px 40px black;\
    font-weight: bolder; \
    }";

function printTime() {
    var d = new Date();
    var hours = d.getHours();
    var mins = d.getMinutes();
    var secs = d.getSeconds();
    document.body.innerHTML = "<table /><td />"+hours+":"+mins+":"+secs;+"</td /></table /><br />"
    
    document.body.appendChild(sheet);
  }

setInterval(printTime, 1000);