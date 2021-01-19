// //Ex1
// let myFavoriteColors = ["blue", "black", "grey", "yellow"];
// let suffix = {
//   1: "st",
//   2: "nd",
//   3: "rd",
//   4: "th"
// };

// for (let i = 0; i < myFavoriteColors.length; i++) {
//   const element = myFavoriteColors[i];
//   if ((i + 1) == 1) {
//     const element = myFavoriteColors[i];
//     console.log('My 1' + suffix["1"] + ' choice is ' + element);
//   } else if ((i + 1) == 2) {
//     const element = myFavoriteColors[i];
//     console.log('My 2' + suffix["2"] + ' choice is ' + element);
//   } else if ((i + 1) == 3) {
//     const element = myFavoriteColors[i];
//     console.log('My 3' + suffix["3"] + ' choice is ' + element);
//   } else {
//     const element = myFavoriteColors[i];
//     console.log('My ' + (i + 1) + suffix["4"] + ' choice is ' + element);
//   }
// }


//Ex2
let people = ["Greg", "Mary", "Devon", "James"];
let peopleCopy = [];
//1
for (const i in people) {
  if (Object.hasOwnProperty.call(people, i)) {
    const element = people[i];
    console.log (element);
  }
}
//2
people.shift();
//3
people.splice(2,2,"Jason");
console.log(people);
//4
people.push("Mike");
console.log(people);
//5
for (const i in people) {
  if (Object.hasOwnProperty.call(people, i)) {
    const element = people[i];
    if (element == "Jason") {
      break;
    }else {
      console.log (element);
    }
  }
}
//6
peopleCopy = people.slice(1,people.length-1);
console.log("Copy of array without Mary and my name Mike: " + peopleCopy);

//Same but no matter where Mary and Mike are positioned in the array
let peopleCopyIn = [];
let peopleIn = ["Hello", "Mary", "Devon", "Jason", "Mike", "Raoul"]
console.log(peopleIn);

for (let i = 0; i < peopleIn.length; i++) {
  const element = peopleIn[i];
  if (element == "Mary" || element == "Mike") {
    continue;
  }else {
    peopleCopyIn.push(element);
  }
}
console.log("Copy of array without Mary and my name Mike: " + peopleCopyIn);

// //7
// console.log("the index of Mary is "+people.indexOf("Mary"));

// //8
// console.log("the index of Foo is "+people.indexOf("Foo"));

// //9
// let last = people[people.length - 1];
// console.log(last);

// //Ex3
// let answer;
// do {
//   answer = prompt("Enter a number between 0 to 20:");
// }
// while (answer < 10);


// //Ex4
// let guestList = {
//   Randy: "Germany",
//   Karla: "France",
//   Wendy: "Japan",
//   Norman: "England",
//   Sam: "Argentina"
// }

// let student = prompt("Please, enter your name:");
// if (student in guestList){
//   console.log("Hi! I'm " + student + ", and I'm from " + guestList[student] +".");
// }else{
//   console.log("Hi! I'm a guest.");
// }


// //Ex5
// let family = {
//   father: "Michael",
//   mother: "Anael",
//   daughter: "Noa",
//   son: "Ben"
// }

// console.log("The properties are ")
// for (const i in family) {
//   console.log(i);
// }

// console.log("The values are ")
// for (const i in family) {
//   console.log(family[i]);
// }

// //Ex6
// let names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// names = names.sort();
// let groupSociety = [];

// for (const i in names) {
//   if (Object.hasOwnProperty.call(names, i)) { 
//     const element = names[i];
//     let firstLetter = element.charAt(0);
//     groupSociety.push(firstLetter);
//   }
// }
// console.log ("The name of the secret group is: "+groupSociety.join(""));