let fruits = ["Banana", "Apples", "Oranges", "Blueberries"];

//remove the banana from the array
fruits.splice(0,1);
console.log (fruits);

//Sort the array in order
fruits.sort();
console.log (fruits);

//put kiwi at the end of the array
fruits.push("Kiwi");
console.log (fruits);

//remove apples from the array with different method
fruits.shift();
console.log (fruits);

//Sort the array in reverse order.
fruits.reverse();
console.log (fruits);

let moreFruits = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];

//access the item oranges
console.log(moreFruits[1][1]);