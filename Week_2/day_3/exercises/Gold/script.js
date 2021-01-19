// //Ex1
// let building = {
//   number_levels : 4,
//   number_of_apt_by_level : {
//       "1": 3,
//       "2": 4,
//       "3": 9,
//       "4": 2,
//   },
//   name_of_tenants : ["Sarah", "Dan", "David"],
//   number_of_rooms_and_rent:  {
//       "Sarah": [3, 990],
//       "Dan":  [4, 1000],
//       "David": [1, 500],
//   },
// }

// //1
// console.log("the number of levels in the building is "+ building['number_levels']);

// //2
// console.log("the number of apartments on level 1 is "+ building['number_of_apt_by_level'][1]);
// console.log("the number of apartments on level 3 is "+ building['number_of_apt_by_level'][3]);

// //3
// console.log("the name of the second tenant is "+ building['name_of_tenants'][1] + " and he has  " + building['number_of_rooms_and_rent']["Dan"][0] + " rooms");

// //4
// let rentSarah = building['number_of_rooms_and_rent']["Sarah"][1];
// let rentDan = building['number_of_rooms_and_rent']["Dan"][1];
// let rentDavid = building['number_of_rooms_and_rent']["David"][1];

// if (rentSarah + rentDavid > rentDan){
//   let answer = prompt ('How much do you want to increase the rent of Dan ?');
//   rentIncrease = Number(answer);
//   newRentDan = rentDan + rentIncrease;
//   building['number_of_rooms_and_rent']["Dan"][1] = newRentDan;
// }

// console.log (building);

// Ex2
let isDivisible;
let answer = prompt('Please enter a number greater than 0 :');
let counter = 0;
let theNumber;

for (i=0;i<answer.length;i++){
  theNumber = answer.substr(i,1);
  counter += Number(theNumber);
}

if (counter % 3 == 0){
  isDivisible =true;
  console.log (answer + " -> " + isDivisible)
} else {
  isDivisible =false;
  console.log (answer + " -> " + isDivisible)
}

// for (i=0;i<answer.length;i++){
//   theNumber = answer.charAt(i);
//   console.log(theNumber);
//   counter += Number(theNumber);
//   console.log("counter "+counter);
// }
// console.log(counter%3);
// if (counter % 3 == 0){
//   isDivisible =true;
//   console.log (answer + " -> " + isDivisible)
// } else {
//   isDivisible =false;
//   console.log (answer + " -> " + isDivisible)
// }
