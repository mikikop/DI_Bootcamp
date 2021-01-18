// // OBJECTS : access the element by the property
// let user = {
// 	username : "John",
// 	password : 1234,
// 	email : "john@gmail.com",
// 	logIn : true,
// 	countries : ["israel", "usa"],
// 	friends : {
// 		names : ["David", "Sarah"]
// 	}
// }

// console.log(user);
// // 1. display the friends nested object
// console.log(user["friends"]);
// // 2. display the list of names of his friends
// console.log(user["friends"]["names"]);
// // 3. display the name of best friend : David
// console.log(user["friends"]["names"][0]);


// // ARRAY OF OBJECTS
// let users = [
// 	{
// 		username : "John",
// 		password: 1234
// 	},
// 	{
// 		username : "Lea",
// 		password: 2222
// 	},
// 	{
// 		username : "David",
// 		password: 6767
// 	}
// ];

// console.log(users)
// // 1. display the information of the 2nd user (object)
// console.log(users[1]);

// // 2. display the password of the 2nd user
// console.log(users[1]["password"]);

// let age = prompt("Hi, How old are you?");

// if (age > 18) {
// 	alert("Powering On. Enjoy the ride!");
// } else if (age ==18) {
// 	alert("Congratulations on your first year of driving. Enjoy the ride!");
// } else {
// 	alert("Sorry, you are too young to drive this car. Powering off")
// }

// // assign to a the value 4
// let a = 2 + 2;

// //check the cases and will display Exactly as an alert
// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }

// assign to a the value 4
let a = 2 + 2;

//check the cases and will display Right as an alert
switch (a) {
  case 4:
    alert('Right!');
    break;

  case 3: // (*) grouped two cases
  case 5:
    alert('Wrong!');
    alert("Why don't you take a math class?");
    break;

  default:
    alert('The result is strange. Really.');
}