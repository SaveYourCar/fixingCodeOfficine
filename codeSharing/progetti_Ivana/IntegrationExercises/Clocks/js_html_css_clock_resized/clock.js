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
  }

setInterval(printTime, 1000);