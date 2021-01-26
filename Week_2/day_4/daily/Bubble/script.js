const numbers = [5, 0, 9, 1, 7, 4, 2, 6, 3, 8];

//1
let num = [];
for (const key in numbers) {
    if (Object.hasOwnProperty.call(numbers, key)) {
        const element = numbers[key];
        num[key] = element.toString();
    }
}
console.log(num);

//2
let numString = num.join("+");
numString = num.join(" ");
numString = num.join("");

console.log(numString);

//3
//ascending order
function bubbleSortAsc(array) {
    let n = array.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (array[j] > array[j + 1]) {
                let variable = array[j];
                array[j] = array[j + 1];
                array[j + 1] = variable;
            }
        }
    }
    return array;
}

console.log(bubbleSortAsc(numbers));

//descending order
function bubbleSortDesc(array) {
    let n = array.length;

    for (let i = 0; i < n; i++) {
        for (let j = 0; j < n; j++) {
            if (array[j] < array[j + 1]) {
                let variable = array[j];
                array[j] = array[j + 1];
                array[j + 1] = variable;
            }
        }
    }
    return array;
}

console.log(bubbleSortDesc(numbers));

//ascending order Optimization
function bubbleSortAscOpt(array) {
    let n = array.length;
    let sorted = false;

    while (!sorted) {
        sorted = true;
        for (let i = 0; i < n; i++) {
            if (array[i] > array[i+1]) {
                let variable = array[i];
                array[i] = array[i+1];
                array[i+1] = variable;
                sorted = false;
            }
        }
        return array;

    }
}

console.log(bubbleSortAscOpt(numbers));