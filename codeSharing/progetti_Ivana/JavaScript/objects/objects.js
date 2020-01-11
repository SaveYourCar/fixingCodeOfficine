/*Objects are lists of values that are written as 
name: value pairs,
with the names and the values separated by colons.
Values are called properties. 
JavaScript objects are containers for named values.*/

var person = {
    name: "John", age: 31, 
    favColor: "green", height: 183
   };

var x = person.age;
var y = person['age'];

document.write("<br />After definig an object 'person', we are printing the property age: " + x);
document.write("<br />Then, we are verifing if \
    the 2 ways, of accessig properties, are effectively equal: " + (x==y));

var course = {name: "JS", lessons: 41};

document.write("<br />We are printing the lenght of the person name,\
    through the build in method, length: " + course.name.length);

/*Methods are functions that are stored as object properties.
 You can also define the function outside of the constructor 
function and associate it with the object. */
/*standard way to create an "object type" 
is to use an object constructor function. */

function person2(name, age, color) {
    this.name = name;
    this.age = age;
    this.favColor = color;
    this.yearOfBirth = bornYear;
    this.changeName = function (name) {
        this.name = name;
    };
  }
function bornYear() {
    return 2020 - this.age;
  };

var p1 = new person2("John", 32, "green");
var p2 = new person2("Amy", 21, "red");

document.write("<br />We are printing the property \
    name of the object p1: " + p1.name)

p1.changeName("Ivana");

document.write("<br />We are changing the name of the object p1 \
    through the method changeName: " + p1.name )

document.write("<br />We are using the method, defined outside the object, \
    bornYear, to get the property p1.yearOfBirth : " + p1.yearOfBirth() )

/*Objects consist of properties,
which are used to describe an object. 
Values of object properties can either contain
primitive data types or other objects. */