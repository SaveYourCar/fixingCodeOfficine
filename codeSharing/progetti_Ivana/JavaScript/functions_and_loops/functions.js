//Functions
 function myFunction() {
    alert("Calling a Function!");
 }

 myFunction()
   /*You can also call a function using this syntax:
    myFunction.call(). 
    The difference is that when calling in this way,
    you're passing the 'this' keyword to a function. */

//Function Parameters
 function sayHello(name) {
    alert("Hi, " + name );
 }
 
 sayHello("Everyone");

 function test(x, y) {
    if(x>y) {
      document.write(x);
    }
    else {
      document.write(y);
    }
 }

 test(5, 8);
    /*When calling the function, 
    provide the arguments in the same order 
    in which you defined them.
     If you pass more arguments than are defined, 
    they will be assigned to an array called arguments.
     They can be used like this: arguments[0], arguments[1],
    etc. 
     If a function is called with missing arguments (fewer than declared),
    the missing values are set to undefined. */
 function sayHello2(name, age) {
    document.write( "<br />" + name + " is " + age + " years old.");
 }

 sayHello2("Ivana", 31)

//Function Return
 function myFunction2(a, b) {
    return a * b;
 }
 
 var x = myFunction2(5, 6); 
 document.write("<br />" + x + "<br />");
    /*If you do not return anything from a function,
    it will return undefined. */

//The Alert Box
 alert("Hello\nHow are you?");

//Prompt Box
 var user = prompt("Please enter your name");
 alert(user);

//Confirm Box
 var result = confirm("Do you really want to leave this page?");
 if (result == true) {
    alert("Thanks for visiting");
 }
 else {
    alert("Thanks for staying with us");
 }

//Example of functins and conditionals

 //While
 function test(number)
 {
   while(number < 5)  {
      number++;
   }
   return number;
 }

 alert(test(2));

 //If
 function test2(a, b) {
    if(a > b) {
      return a*b; 
  } else {
       return b / a; 
      }
  }

  alert(test2(5, 15));

 //Switch
 function choose_color(color_name){
   switch(color_name) {
   case "blue": 
     alert("This is blue.");
     break;
   case "red": 
     alert("This is red.");
     break;
   case "green": 
     alert("This is green."); 
     break;
   case "orange": 
      alert("This is orange."); 
      break;
   default: 
      alert("Color not found.");
   }
 }

 color_name = prompt("choose color")
 choose_color(color_name)

 //For
  function print_numbers(max_number){
    for (i=1; i<=max_number; i++) {
        document.write(i + "<br />");
     }
  }

  max_number=prompt("enter number")
  print_numbers(max_number)
 
  //Do...While 
  function print_numbers_selction(max_number,i){
    do {  
      document.write(i + "<br />");
      i--;  
    }
    while (i<=max_number && i>0); 
  }
  max_number=prompt("enter max number")
  i=prompt("enter number")
  print_numbers_selction(max_number,i)