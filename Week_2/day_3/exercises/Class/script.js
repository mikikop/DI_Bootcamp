//Ex1
for (let i = 0; i <= 15; i++) {
  if (i%2 == 0) {
    console.log(i + " is even");
  } else {
    console.log(i + " is odd");
  }
}

//Ex2
//use a for loop to console.log each name and say hello
//'hello lea'
let friends = ["Lea", "Jonas", "David"];
for (let i = 0; i < friends.length; i++) {
  const element = friends[i];
  console.log('Hello '+element);
}