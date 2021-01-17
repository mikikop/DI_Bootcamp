//exercise 1
let addressNumber = "3";
console.log("My address number is " + addressNumber);

let addressStreet = "Shwartz street";
console.log ("My address street is "+ addressStreet);

let country = "Israel";
console.log ("my country is " + country);

let global_address = "I live in " + addressStreet + " " + addressNumber + ", in " + country;
console.log (global_address);

//exercise 2
let birth_year = 1977;
let future_year = 2050;

let myFutureAge = future_year - birth_year;
console.log( "I will be " + myFutureAge + " in "+ future_year);

//exercise 3
let pets = ["cat","dog", "fish", "rabbit", "cow"];
console.log (pets[1]);
pets.push("horse");
console.log(pets);
pets.splice(3,1);
console.log(pets);
console.log(pets.length);