var cssId = 'myCss'; 
if (!document.getElementById(cssId))
{
    var head  = document.getElementsByTagName('head')[0];
    var link  = document.createElement('link');
    link.id   = cssId;
    link.rel  = 'stylesheet';
    link.type = 'text/css';
    link.href = 'clock.css';
    link.media = 'all';
    head.appendChild(link);
}

function printTime() {
    var d = new Date();
    var hours = d.getHours();
    var mins = d.getMinutes();
    var secs = d.getSeconds();
    document.body.innerHTML = 
      "<table /><td />"+hours+":"+mins+":"+secs;+"</td /></table /><br />"
    
    document.body.appendChild(sheet);
  }

setInterval(printTime, 1000);

var images = [
  "https://images.unsplash.com/photo-1445998559126-132150395033?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1875&q=80", 
  "https://images.unsplash.com/photo-1575761344173-aa186491c120?ixlib=rb-1.2.1&auto=format&fit=crop&w=1950&q=80", 
  "https://images.unsplash.com/photo-1575251664080-ba2afe7e337a?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80"
];

var num = 0;
  
function next() {
    num++;
    if(num >= images.length) {
      num = 0;
    };
    document.body.style.backgroundImage= "url("+images[num]+")";
    document.body.appendChild(sheet);
    
    };



setInterval(next, 10000);