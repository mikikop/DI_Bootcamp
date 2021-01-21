let answer = prompt ("enter the operations you want to calculate in the format: x + y - don't forget the space between every arguments");
let tabOper = answer.split(" ");

function my_f(arg){
    if(typeof arg == "number"){
        return Number(arg);
    }else{
        return arg;
    }
}

function calc (arg1,arg2,arg3){
    switch(arg2){
        case "+":
            return eval (`${arg1} + ${arg3}`);
            break;
        case "-":
            return eval (`${arg1} - ${arg3}`);
            break;
        case "*":
            return eval (`${arg1} * ${arg3}`);
            break;
        case "/":
            return eval (`${arg1} / ${arg3}`);
            break;
    }
}

let firstOp = my_f(tabOper[0]);
let secondOp = my_f(tabOper[1]);
let thirdOp = my_f(tabOper[2]);

let result = calc(firstOp,secondOp,thirdOp);
console.log(`The result of ${answer} is ${result}`);