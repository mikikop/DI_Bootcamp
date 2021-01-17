let strNum = prompt ("Please enter a string of numbers separated by a comma and space !");
let array = strNum.split(", ");
let result = 1;

for (const key in array) {
    if (Object.hasOwnProperty.call(array, key)) {
        result = result * Number(array[key]);
    }
}

alert("The product of all your numbers is "+result);
