var x = 10;
document.write(x);
/*-When you change the value of x one time, 
it will automatically be changed in all places where you used it
Naming rules:
- The first character must be a letter,
 an underscore (_), or a dollar sign ($).*/
var price = 55.55;
document.write('\n',price);
var name = 'John';
var text = "My name is ";
var sayHello = '\nHello world! \'I am a JavaScript programmer.\' ';
document.write('\n',text,name,sayHello);
/*-You can use quotes inside a string, 
as long as they don't match the quotes surrounding the string.
-You can get double quotes inside of double quotes 
using the escape character like this:
 \" or \' inside of single quotes.*/
var isActive = true; 
var isHoliday = false;
/*-The Boolean value of 0 (zero), null, undefined,
empty string is false.
Everything with a "real" value is true.*/
var x = 10 + 5;
document.write('\nx=',x);
var x = 10 * '5';
document.write('\nx=',x);
var y = 100 / 5;
document.write('\ny=',y);
var myVariable = 26 % 6;
document.write('\n',myVariable++);
document.write(++myVariable);
document.write(--myVariable);
x -= y += 9;
document.write('\nx=',x,'\ny=',y);
/*-You can get the result of a string expression using the eval() function,
which takes a string expression argument like
eval("10 * 20 + 8") and returns the result. 
If the argument is empty, it returns undefined.
-10 * '5' or '10' * '5' gives the same result. 
Multiplying a number with string values like 'learn' * 5 returns 
NaN (Not a Number).*/
var num = 10; 
document.write('\n',num == 8);
document.write('\n',num == '10');
document.write('\n',num === '10');
// === means identical, equal and from the same type.
document.write('\n',num === '10' && num==10); //return false
document.write('\n',num === '10' || num==10); //return true
document.write('\n',!(num === '10')); //return true
var age = 17;
var isAdult = (age < 18) ? "Too young": "Old enough";
document.write('\n',isAdult);
//Logical operators allow you to connect as many expressions as you wish.
var mystring1 = "I am learning ";
var mystring2 = "JavaScript";
document.write('\n'+mystring1 + mystring2);