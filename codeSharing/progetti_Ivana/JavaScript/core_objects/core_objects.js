/*Arrays*/
/*Arrays store multiple values in a single variable. */
document.write("<h1 />Arrays</h1 /><br />");

var courses = new Array("HTML", "CSS", "JS"); 

document.write("<p />After declaring a "+"<strong />new array</strong />"+", named 'courses', \
    we are printing his third entry:\
    "+"<strong />"+courses[2]+"</strong />"+"</p /><br />");

courses[1] = "C++"; //Changes the second element 

/*You can also declare an array, 
tell it the number of elements it will store, 
and add the elements later. */

var courses2 = new Array(3);
courses2[0] = "HTML";
courses2[1] = "CSS";
courses2[2] = "JS";

/*JavaScript arrays are dynamic, 
so you can declare an array and not pass any arguments
with the Array() constructor.
You can then add the elements dynamically.*/

document.write("<p />After declaring a new array, named 'courses2', \
    with 3 entries,\ we "+"<strong />declared the entries later</strong />"+", \
    then we are printing the first entry:\
    "+"<strong />"+courses2[0]+"</strong />"+"</p /><br />");

courses2[3] = "Python";
document.write("<p />Next we added a forth element: \
    "+"<strong />"+courses2[3]+"</strong />"+"</p /><br />");

var courses3 = new Array();
courses3[0] = "C#";
courses3[1] = "Python";

/*Attempting to access an index outside of the array,
returns the value undefined.
An array is a special type of object.
An array uses numbers to access its elements, 
and an object uses names to access its members.  */

/*Array Literal
For greater simplicity, readability, and execution speed,
you can also declare arrays using the array literal syntax.
The array literal syntax is 
the recommended way to declare arrays. */

var courses4 = ["HTML", "CSS", "JS"]; 
document.write("<p />We created a new arrey with"+"<strong /> the literal syntax</strong />"+", \
    we access his entries through his indexes. This is his second entry:\
    "+"<strong />"+courses4[1]+"</strong />"+"</p /><br />");

/*The length Property:
An array's length property returns the number of it's elements. */

document.write("<p />We used "+"<strong />the lenght property</strong />"+", to get  \
    the lenght of our first declared array:\
    "+"<strong />"+courses.length+"</strong />"+"</p /><br />");

/*Combining Arrays:
JavaScript's concat() method allows you to join arrays
and create an entirely new array. */

var courses = courses3.concat(courses4);

document.write("<p />We used "+"<strong />the concat property</strong />"+", to get  \
    a new array as union of 2 old ones.\
    Now our courses array looks like this:\
    "+"<strong />"+courses+"</strong />"+"</p /><br />");

/*Associative Arrays:
you can use the named array syntax,
to acces the entry of an array 
which will produce an object. */

var person = [];
person["name"] = "John";
person["age"] = 46;

document.write("<p />We used "+"<strong />the named array syntax</strong />"+", to get  \
    to set the entries, name and age, of a 'person' array.\
    Doing this we created an object person. \
    The age of this person is: \
    "+"<strong />"+person["age"]+"</strong />"+"</p /><br />")
/*As the person array is treated as an object,
the standard array methods and properties 
will produce incorrect results. 
For example, person.length will return 0.
N.B. It is better to use an object 
when you want the index to be a string (text).
Use an array when you want the index to be a number. */

/*The Math Object */
document.write("<h1 />The Math Object</h1 /><br />");

/*Math has no constructor. 
There's no need to create a Math object first. */

/*PI */

document.write("<p />We used the Math method "+"<strong />PI</strong />"+", to get  \
    an evaluation of the PI number: \
    "+"<strong />"+Math.PI+"</strong />"+"</p /><br />")
document.write("<p />We used the Math method "+"<strong />E</strong />"+", to get  \
    an evaluation of the Euler's Costant: \
    "+"<strong />"+Math.E+"</strong />"+"</p /><br />")
document.write("<p />We used the Math method "+"<strong />LN2</strong />"+", to get  \
    an evaluation of the Natural log of the value 2: \
    "+"<strong />"+Math.LN2+"</strong />"+"</p /><br />")

    
/*Math Object Methods*/

var number = Math.sqrt(4); 

document.write("<p />We used the Math method "+"<strong />sqrt</strong />"+", to get  \
        the square root of the number 4: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.abs(-5); 

document.write("<p />We used the Math method "+"<strong />abs</strong />"+", to get  \
    the absolute values of the number -5: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.ceil(5.5); 

document.write("<p />We used the Math method "+"<strong />ceil</strong />"+", to get  \
    the rounded upward values of the number 5.5: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.floor(5.5); 

document.write("<p />We used the Math method "+"<strong />floor</strong />"+", to get  \
    the rounded downward values of the number 5.5: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.floor(5.5); 

document.write("<p />We used the Math method "+"<strong />round</strong />"+", to get  \
    the nearest integer of the number 5.5: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")
    

var number = Math.max(1,3,1,2,8,8); 

document.write("<p />We used the Math method "+"<strong />max</strong />"+", to get  \
    the max value of the list o number: (1,3,1,2,8,8). \
    The result is: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.min(1,3,1,2,8,8); 

document.write("<p />We used the Math method "+"<strong />min</strong />"+", to get  \
    the min value of the list o number: (1,3,1,2,8,8). \
    The result is: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.pow(1,3); 

document.write("<p />We used the Math method "+"<strong />pow</strong />"+", to get  \
    the third pow of 1. \
    The result is: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

var number = Math.random();

document.write("<p />We used the Math method "+"<strong />random</strong />"+", to get  \
        a random number beetwen 0 and 1.\
        The result is: \
        "+"<strong />"+number+"</strong />"+"</p /><br />")

/*To get a random number between 1-10, 
use Math.random(), which gives you a number between 0-1. 
Then multiply the number by 10, and then take Math.ceil() from it: 
Math.ceil(Math.random() * 10). */

var number = Math.ceil(Math.random() * 10)

document.write("<p />We used the Math methods "+"<strong />random and ceil</strong />"+", to get  \
    a random integer between 1 and 10. \
    The result is: \
    "+"<strong />"+number+"</strong />"+"</p /><br />")

/*Object that if created will ask the user to input a number 
and alert its square root.*/

function output_sqrt(){
    this.number = prompt("Enter a number", "");;
    this.answer = alert("The square root of " + this.number + " is " 
        + Math.sqrt(this.number));
};

//var alert1 = new output_sqrt();


/*The setInterval method */
/*The setInterval() method calls a function
or evaluates an expression at specified intervals (in milliseconds).
It will continue calling the function until
clearInterval() is called or the window is closed. */

function myAlert() {
    alert("Hi");
 }
//setInterval(myAlert, 3000);

    /*This will call the myAlert function 
    every 3 seconds (1000 ms = 1 second). */


/*The Date Object*/
document.write("<h1 />The Date Object</h1 /><br />");

/*The Date object enables us to work with dates.
A date consists of 
a year, a month, a day, an hour, a minute, a second, and milliseconds.
Using new Date(), create a new date object with the current date and time.*/

var d = new Date();

document.write("<p />we initialize a "+"<strong />Date Object</strong />"+" in a varyable. \
    we are now able to get the current date and time by calling the variable:\
    "+"<strong />"+d+"</strong />"+"</p /><br />");

//Fri Jan 02 1970 00:00:00
var d1 = new Date(86400000); 

document.write("<p />This Date is set using "+
    "<strong />milliseconds</strong />: "
    +"<strong />"+d1+"</strong />"+"</p /><br />");


//Fri Jan 02 2015 10:42:00
var d2 = new Date("January 2, 2015 10:42:00");
document.write("<p />This Date is set using a "
    +"<strong />dateString</strong />: "
    +"<strong />"+d2+"</strong />"+"</p /><br />");


//Sat Jun 11 1988 11:42:00
var d3 = new Date(88,5,11,11,42,0,0);
document.write("<p />This Date is set using a "
    +"<strong />year, month, day, hours, minutes, seconds, milliseconds</strong />: "
    +"<strong />"+d3+"</strong />"+"</p /><br />");

/*JavaScript counts months from 0 to 11. 
January is 0, and December is 11.
Date objects are static, rather than dynamic.
The computer time is ticking, but date objects don't change, once created. */

/*Date Methods */

var hours = d.getHours();

document.write("<p />We used the "
    +"<strong />getHours</strong /> method to get the current hour: "
    +"<strong />"+hours+"</strong />"+"</p /><br />");

var minutes = d.getMinutes();

document.write("<p />We used the "
    +"<strong />getMinuts</strong /> method to get the current hour's minutes: "
    +"<strong />"+minutes+"</strong />"+"</p /><br />");

var year = d.getFullYear();

document.write("<p />We used the "
        +"<strong />getFullYear</strong /> method to get the current year: "
        +"<strong />"+year+"</strong />"+"</p /><br />");

//program that prints the current time to the browser once every second.

function printTime() {
    var d = new Date();
    var hours = d.getHours();
    var mins = d.getMinutes();
    var secs = d.getSeconds();
    document.body.innerHTML = hours+":"+mins+":"+secs;
  }

//setInterval(printTime, 1000);
/*The innerHTML property sets or returns the HTML content of an element.
In our case, we are changing the HTML content of our document's body.
This overwrites the content every second, 
instead of printing it repeatedly to the screen. */




    




