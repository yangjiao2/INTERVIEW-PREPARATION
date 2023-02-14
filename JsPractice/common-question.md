closure:
var num = 10;
function sum()
{
 console.log(num);
}
sum();

// 10


str.charAt(4);


// Undefined
typeof undefined;  // Returns: "undefined"
typeof undeclaredVariable; // Returns: "undefined"
// Null
typeof Null;  // Returns: "object"
// Objects
typeof {name: "John", age: 18};  // Returns: "object"
// Arrays
typeof [1, 2, 3];  // Returns: "object"
// Functions
typeof function(){};  // Returns: "function"

--

`event.preventDefault()` returns boolean = if was called in a particular element.

--


 isNan() function returns true if the variable value is not a number.

isNaN('1')  // Returns false, since '1' is converted to Number type which results in 0 ( a number)
isNaN(true) // Returns false, since true converted to Number type results in 1 ( a number)
isNaN(false) // Returns false

--

assign a  = b is pass by referencce if it is non-primitive data types: object

--

function doSomething() {
  console.log(this);
}

doSomething(); // global



var obj = {
    name:  "vivek",
    getName: function(){
    console.log(this.name);
  }
}

obj.getName(); // vivek
