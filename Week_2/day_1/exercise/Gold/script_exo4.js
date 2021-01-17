let num1 = Number(prompt("Please enter a first number: "));
let num2 = Number(prompt("Please enter a second number:"));
let operator = prompt("Please choose an operator to calculate between number 1 and number 2: (+,-,*,/)");


if (operator == "+") {
    alert(num1 + num2);
} else if (operator == "-") {
    if (num1 >= num2) {
        alert(num1 - num2);
    } else {
        alert("Your first number is smaller than the second one and we can't substract them");
    }
} else if (operator == "*") {
    alert(num1 * num2);
} else if (operator == "/") {
    if (num2 !== 0) {
        alert(num1 / num2);
    } else {
        alert("The division by 0 is impossible");
    }
}
