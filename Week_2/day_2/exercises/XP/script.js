//Ex 1
let x = 12;
let y = 11;

if (x>y) {
    console.log(x + " is bigger than "+ y);
} else if (x<y) {
    console.log(y + " is bigger than "+ x);
}else {
    console.log(x + " is equal to "+ y);
}

//Ex2
let newDog = "Chihuahua";
let counter = newDog.length;
console.log("There are " + counter + " letters in "+ newDog);
console.log(newDog.toUpperCase());
console.log(newDog.toLowerCase());
if (newDog === "Chihuahua") {
    console.log("I love Chihuahua, it’s my favorite dog breed");
}else {
    console.log("I dont care, I prefer cats");   
}

//Ex3
let num = prompt("Please enter a number ! ");
if (num%2 == 0) {
    alert(num + " is an even number");
} else {
    alert(num + " is not an even number");
}

//Ex4
let users = ["Lea123", "Princess45", "cat&doglovers", "helooo@000"]
if (!(Array.isArray(users) && users.length)) {
    console.log("no one is online");
}else if (users.length == 1) {
    console.log(users[0] + " is online");
} else if (users.length == 2) {
    console.log(users[0] + " and " + users[1] + " are online");
} else {
    console.log(users[0] + ", " + users[1] + " and " + ((users.length) - 2) + " more are online");
}