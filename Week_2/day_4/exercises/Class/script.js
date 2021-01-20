//Exo1
function parentAge (myAge){
    let mumAge = myAge*2;
    let dadAge = mumAge*1.2;
    console.log (`my mum age is ${mumAge}`);
    console.log (`my dad age is ${dadAge}`);
}

parentAge (26);


//Exo2
function mumAge (myAge){
    let mumAge = myAge*2;
    return mumAge;
}

//1st way
console.log(mumAge(26));

//2nd way
let my_mum_Age = mumAge (26);
console.log(`the age of my mum is ${my_mum_Age}`);