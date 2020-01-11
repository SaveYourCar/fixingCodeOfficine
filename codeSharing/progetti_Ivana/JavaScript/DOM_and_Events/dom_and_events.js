/*The DOM */
/*DOM = Document Object Model
JavaScript can be used to manipulate 
the DOM of a page dynamically to add,
delete and modify elements. */
/*
<html> has two children (<head>, <body>);
<head> has one child (<title>) and one parent (<html>);
<title> has one parent (<head>) and no children;
<body> has two children (<h1> and <a>) and one parent (<html>); 
*/

//document.body.innerHTML = "Some text";

/*the document object is the owner 
(or root) of all objects in your webpage.
So, if you want to access objects in an HTML page,
you always start with accessing the document object. */

//finds element by id
//document.getElementById(id) 

//finds elements by class name
//document.getElementsByClassName(name) 

//finds elements by tag name
//document.getElementsByTagName(name)

//var elem = document.getElementById("demo");
//elem.innerHTML = "Hello World!";
/*
var arr = document.getElementsByTagName("p");
for (var x = 0; x < arr.length; x++) {
  arr[x].innerHTML = "Hi there";
}
*/
//Selecting Elements
var a = document.getElementById("demo");
var arr = a.childNodes;
for(var x=0;x<arr.length;x++) {
  arr[x].innerHTML = "The text in this paragraph\
   has been changed through <strong />.childNodes</strong />";
};

//Changing elements

var el = document.getElementById("myimg");
el.src = "https://images.unsplash.com/photo-1577083165350-16c9f88b4a25?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=500&q=60";

/*Practically all attributes of an element 
can be changed using JavaScript.  */

//Changing Style

var x = document.getElementById("demo2");
x.style.color = "brown";
x.style.width = "100px";

/*All CSS properties can be set and modified using JavaScript.
Just remember, that you cannot use dashes (-) in the property
names: these are replaced with camelCase versions, 
where the compound words begin with a capital letter.
For example: the background-color property should be referred
to as backgroundColor. */

//Adding & Removing Elements

/*Use the following methods to create new nodes:
element.cloneNode() clones an element and returns the resulting node.
document.createElement(element) creates a new element node.
document.createTextNode(text) creates a new text node. */

//var node1 = document.createTextNode("This content its added after the elements creation");

/*
This will create a new text node,
but it will not appear in the document until
you append it to an existing element with
one of the following methods:
element.appendChild(newNode)
 adds a new child node to an element as the last child node.
element.insertBefore(node1, node2)
 inserts node1 as a child before node2. */

//creating a new paragraph
var p = document.createElement("p");
var node = document.createTextNode("This text is created .createTextNode");
//adding the text to the paragraph
p.appendChild(node);

var div = document.getElementById("demo3");
//adding the paragraph to the div
div.appendChild(p);

//Removing Elements
/*To remove an HTML element,
you must select the parent of the element
and use the removeChild(node) method. */

var parent = document.getElementById("demo4");
var child = document.getElementById("p1");
parent.removeChild(child);

/*An alternative way of achieving the same result
would be the use of the parentNode property 
to get the parent of the element we want to remove:
var child = document.getElementById("p1");
child.parentNode.removeChild(child); */

/*Replacing Elements

To replace an HTML element, the 
element.replaceChild(newNode, oldNode) method is used.
For example: */

var p = document.createElement("p");
var node = document.createTextNode("This new node replaced an older one: .replaceChild(p, child)");
p.appendChild(node);

var parent = document.getElementById("demo5");
var child = document.getElementById("p1");
parent.replaceChild(p, child);

//Creating Animations

/*This code creates a timer that calls a move()
function every 500 milliseconds.
Now we need to define the move() function, 
that changes the position of the box.  
The move() function increments the left property 
of the box element by one each time it is called.*/

// starting position
var pos = 0; 
//our box element
var box = document.getElementById("box");

function move() {
  pos += 1;
  box.style.left = pos+"px"; //px = pixels
}
/*
The following code defines a timer that calls the move() 
function every 10 milliseconds: */

var t = setInterval(move, 10);

//This makes our box move to the right forever
/*To stop the animation when the box reaches the end
of the container, we add a simple check to the move()
function and use the clearInterval() method to stop the timer. */

var pos2 = 0; 
//our box element
var box2 = document.getElementById("box2");
var t2 = setInterval(move_and_stop, 10);

function move_and_stop() {
  if(pos >= 150) {
    clearInterval(t2);
  }
  else {
    pos2 += 1;
    box2.style.left = pos2+"px";
  }
}

/*
When the left attribute of the box reaches the value of 150, 
the box reaches the end of the container,
based on a container width of 200 and a box width of 50. */

//Handling Events

/*You can write JavaScript code that executes when an event occurs,
such as when a user clicks an HTML element,
moves the mouse, or submits a form.
When an event occurs on a target element,
a handler function is executed. 

Examples of events:
https://en.wikipedia.org/wiki/DOM_events

Corresponding events can be added to HTML elements as attributes.
For example: <p onclick="someFunc()">some text</p>
*/

function show() {
  alert("Hi there");
}

/*
Event handlers can be assigned to elements. */

var x = document.getElementById("demo6");
x.onclick = function () {
  document.body.innerHTML = Date();
}

/*The onload and onunload events are triggered
when the user enters or leaves the page. 
These can be useful when performing actions after the page is loaded. 
Events
The onload and onunload events are triggered when 
the user enters or leaves the page. 
These can be useful when performing actions after the page is loaded. 

<body onload="doSomething()">

Similarly, the window.onload event can be used to run code 
after the whole page is loaded.

window.onload = function() {
   //some code } 
   
The onchange event is mostly used on textboxes. 
The event handler gets called when the text inside the textbox 
changes and focus is lost from the element.*/

function change() {
  var x = document.getElementById("name");
  x.value= x.value.toUpperCase();
 }

/*The addEventListener() method
attaches an event handler to an element
without overwriting existing event handlers.
You can add many event handlers to one element.
You can also add many event handlers
of the same type to one element, i.e., two "click" events.

syntax: element.addEventListener(event, function , useCapture);

The third parameter is a Boolean value 
specifying whether to use event bubbling or event capturing. 
This parameter is optional.
Note that you don't use the "on" prefix for this event; 
use "click" instead of "onclick".*/

var element = document.getElementById("demo8");

element.addEventListener("click", myFunction);
element.addEventListener("mouseover", myFunction);

function myFunction() {
  alert("Hello World!");
}

element.removeEventListener("mouseover", myFunction);

/*event handler that removes itself after being executed: */

var btn = document.getElementById("demo7");
btn.addEventListener("click", myFunction2);
btn.addEventListener("mouseover", myFunction2);

function myFunction2() {
  alert(Math.random());
  btn.removeEventListener("click", myFunction2);
}

/*Internet Explorer version 8 and lower do 
not support the addEventListener() and removeEventListener() methods.
However, you can use the document.attachEvent() method 
to attach event handlers in Internet Explorer. */

/*Event Propagation

There are two ways of event propagation in the HTML DOM:
bubbling and capturing. 
Capturing goes down the DOM.
Bubbling goes up the DOM.

In bubbling, 
 the innermost element's event is handled first
 and then the outer element's event is handled. 

In capturing,
 the outermost element's event is handled first and then the inner.


The addEventListener() method allows you to specify
the propagation type with the "useCapture" parameter.

syntax: addEventListener(event, function, useCapture)


The default value is false, 
which means the bubbling propagation is used; 
when the value is set to true, the event uses the capturing propagation.

This is particularly useful 
when you have the same event
handled for multiple elements in the DOM hierarchy.
*/
/*
var elem1 = document.getElementsByClassName("div1")
var elem2 = document.getElementById("par1")
Capturing propagation
elem1.addEventListener("click", myFunction, true); 
elem2.addEventListener("mouseover", myFunction, true); 

Bubbling propagation
elem2.addEventListener("mouseover", myFunction, false);
*/

/*Image Slider */
/*The images will be changed using "Next" and "Prev" buttons. */
var images = [
  "http://www.sololearn.com/uploads/slider/1.jpg", 
  "http://www.sololearn.com/uploads/slider/2.jpg", 
  "http://www.sololearn.com/uploads/slider/3.jpg"
];

var num = 0;

function next() {
  var slider = document.getElementById("slider");
  num++;
  if(num >= images.length) {
    num = 0;
  }
  slider.src = images[num];
  }

function prev() {
  var slider = document.getElementById("slider");
  num--;
  if(num < 0) {
    num = images.length-1;
  }
  slider.src = images[num];
}

/*
The num variable holds the current image. 
The next and previous button clicks are handled 
by their corresponding functions, 
which change the source of the image to the 
next/previous image in the array.
*/

function test() {
  var x=document.getElementById('txt');
  var n = x.innerHTML;
  x.innerHTML = n/2;
}

/*Form Validations

Complex form validation can be done using JavaScript.
The form element has an onsubmit event that can be handled 
to perform validation.
For example, let's create a form with two inputs and one button. 
The text in both fields should be the same
and not blank to pass the validation. */

function validate() {
  var n1 = document.getElementById("num1");
  var n2 = document.getElementById("num2");
  if(n1.value != "" && n2.value != "") {
    if(n1.value == n2.value) {
      return true;
    }
  }
  alert("The values should be equal and not blank");
  return false;
}

/*
We return true only when the values are not blank and are equal.
The form will not get submitted if its onsubmit event returns false.  */





