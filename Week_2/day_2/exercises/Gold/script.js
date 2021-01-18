// //Ex 1
// let language = prompt("Hi, which language are you speaking?");

// switch (language){
//     case 'french':
//         alert('Bonjour');
//         break;
//     case 'english':
//         alert('Hello');
//         break;
//     case 'hebrew':
//         alert('Shalom');
//         break;
//     default:
//         alert('01110011 01101111 01110010 01110010 01111001');
        
// }

// //Ex2
// let grade = prompt("Hi, which grade did you get?");
// if (grade >= 0 && grade<=100) {
//     if (grade < 70) {
//         console.log("your grade is a D")
//     } else if (grade>= 70 && grade <=80){
//         console.log("your grade is a C")
//     } else if (grade > 80 && grade <=90){
//         console.log("your grade is a B")
//     } else {
//         console.log("your grade is a A")
//     }
// }else {
//     console.log("your grade is a greater number than the maximum grade")
// }

//Ex3
let verb = prompt ('Hi, enter a verb without "to"');
let verbLength = verb.length;
let verbEnd = verb.substr(verbLength -3);

if (verbEnd != 'ing'){
    if (verbLength >= 3) {
        console.log(verb+'ing');
    } else {
        console.log(verb);
    }
} else {
    console.log(verb+'ly');
}

