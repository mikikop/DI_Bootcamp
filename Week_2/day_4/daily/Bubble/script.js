const numbers = [5,0,9,1,7,4,2,6,3,8];

//1
let num = [];
for (const key in numbers) {
    if (Object.hasOwnProperty.call(numbers, key)) {
        const element = numbers[key];
        num[key]=element.toString();
    }
}
console.log(num);

//2
let numString = num.join("+");
numString = num.join(" ");
numString = num.join("");

console.log(numString);

//3
let numSorted = [];
let variable;
for(let i=0; i<numbers.length;i++){
    for(let j=0;j<numbers.length;j++){
        if(numSorted[i]>=numbers[j]){
            variable = numSorted[i];
            // console.log(variable);
            // console.log(numSorted);
        }else{
            variable = numbers[j];
            // console.log(variable);
        }
    }
}
numSorted.push(variable);
console.log(numSorted);