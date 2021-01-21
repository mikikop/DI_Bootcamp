//Ex1
//1
let myAge = prompt ('What is your age?');

//2
function checkDriverAge(){
    if (myAge == 18) {
        alert('Congratulations on your first year of driving. Enjoy the ride!');
    } else if(myAge < 18){
        alert('Sorry, you are too young to drive this car. Powering off');
    }else {
        alert('You are old enough to drive, Powering On. Enjoy the ride!');
    }
}

checkDriverAge();


//3
function checkDriverAgeParam(age){
    if (age == 18) {
        alert('Congratulations on your first year of driving. Enjoy the ride!');
    } else if(age < 18){
        alert('Sorry, you are too young to drive this car. Powering off');
    }else {
        alert('You are old enough to drive, Powering On. Enjoy the ride!');
    }
}

checkDriverAgeParam(92);

//Exo2

function changeEnough(change,amount){
    let quarter = 0.25;
    let dime = 0.1;
    let nickel = 0.05;
    let penny = 0.01;
    let myChange = 0;

    myChange = (change[0]*quarter) + (change[1]*dime) + (change[2]*nickel) +
    (change[3]*penny);

    if (myChange > amount) {
        return true;
    }else {
        return false;
    }
}

//let isPurchased = changeEnough([2, 100, 0, 0], 14.11);
let isPurchased = changeEnough([0, 0, 20, 5], 0.75);

console.log (`1st way: ${isPurchased}`);

//Other way:
function myPocketChange(change){
    let quarter = 0.25;
    let dime = 0.1;
    let nickel = 0.05;
    let penny = 0.01;
    let myChange = 0;

   return myChange = (change[0]*quarter) + (change[1]*dime) + (change[2]*nickel) +
    (change[3]*penny);
}

function changeEnough(myChange,amount){
    if (myChange > amount) {
        return true;
    }else {
        return false;
    }
}

let myChange = myPocketChange([2, 100, 0, 0]);
//let myChange = myPocketChange([0, 0, 20, 5]);

let isPurchased2 = changeEnough (myChange,14.11);
//let isPurchased2 = changeEnough (myChange,0.75);

console.log (`2nd way: ${isPurchased2}`);


//Exo3
function chekMultiple (x){
    let tab = [];
    for (i=0; i<=500; i++){
        if (i%x == 0){
            tab.push(i);
        }
    }
    return tab;
}

function sum (tab) {
    let mySum = 0;
    for (const key in tab) {
        if (Object.hasOwnProperty.call(tab, key)) {
            mySum += tab[key];       
        }
    }
    return mySum;
}

let choice = prompt('Give a number you want the find multiples:');
let choiceMultiple = chekMultiple(choice);
let choiceSum = sum (choiceMultiple);
console.log(`Elements : ${choiceMultiple.join(" ")} \n Sum : ${choiceSum}`);


Exo4
let amazonBasket = {
    glasses: 1,
    books: 2,
    floss: 100
}

let choice = prompt ('Which item do you wish ?');

function checkBasket(item){
    if (item in amazonBasket){
        let answer = `the item ${item} is in stock`;
        return answer;
    } else {
        answer = `the item ${item} is not in stock`;
        return answer;
    }
}

alert(checkBasket(choice));

Exo5
//1 way with an object
let shoppingList = { 
    "banana": 6, 
    "apple": 1,
    "orange": 25
}

//2
let stock = { 
    "banana": 6, 
    "apple": 0,
    "pear": 12,
    "orange": 32,
    "blueberry":1
}  

let prices = {    
    "banana": 4, 
    "apple": 2, 
    "pear": 1,
    "orange": 1.5,
    "blueberry":10
} 

//3
function myBill() {
    let priceBanana = shoppingList["banana"] * prices["banana"];
    let priceApple  = shoppingList["apple"] * prices["apple"];
    let priceOrange = shoppingList["orange"] * prices["orange"];
    let totalPrice = priceBanana + priceApple + priceOrange;
    return totalPrice;
}

//4
let sprentPrice = myBill();
console.log(`the price spent of my shopping list is $${sprentPrice}`);

//5
function myBill() {
    let priceBanana;
    let priceApple;
    let priceOrange;

    //check le stock
    if (stock["banana"]>=shoppingList["banana"]){
        stock["banana"] -= shoppingList["banana"];
        priceBanana = shoppingList["banana"] * prices["banana"];
    } else {
        priceBanana = 0;
    }   
    
    if (stock["apple"]>=shoppingList["apple"]){
        stock["apple"] -= shoppingList["apple"];
        priceApple = shoppingList["apple"] * prices["apple"];
    } else {
        priceApple = 0;
    } 

    if (stock["orange"]>=shoppingList["orange"]){
        stock["orange"] -= shoppingList["orange"];
        priceOrange = shoppingList["orange"] * prices["orange"];
    } else {
        priceOrange = 0;
    } 

    let totalPrice = priceBanana + priceApple + priceOrange;
    return totalPrice;
}
let sprentPrice = myBill();
console.log(`the price spent of my shopping list is $${sprentPrice}`);
console.log(stock);

//Exo6
let answer = prompt('Please enter the amount of 3 bills you have separated by a comma');
let tabAmount = answer.split(",");

function tipBill (tab){
    let tipTab =[];
    for (let i = 0; i < tab.length; i++) {
        if(tab[i]<50){
            tipTab[i] = tab[i]*0.2;
        }else if(tab[i]>=50 && tab[i]<200){
            tipTab[i] = tab[i]*0.15;
        }else {
            tipTab[i] = tab[i]*0.1;
        }
    }
    return tipTab;
}

let tipArray = tipBill(tabAmount);
let totalAmount=[];
for (i=0;i<tabAmount.length;i++){
    totalAmount[i] =Number(tabAmount[i])+Number(tipArray[i]);
}
console.log(`the tips for the 3 bills are ${tipArray}`);
console.log(`the total amount to pay for each bill is ${totalAmount}`);

Ex7
