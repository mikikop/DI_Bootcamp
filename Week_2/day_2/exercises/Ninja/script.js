// //Ex1
// let date1 = prompt('give me the first year of birth in the format YYYY');
// let date2 = prompt('give me the second year of birth in the format YYYY');
// let differenceAge;
// let dateFirst = Number(date1);
// let dateSecond = Number(date2);

// if (dateFirst > dateSecond) {
//     differenceAge = dateFirst - dateSecond;
//     let dateHalf = dateFirst + differenceAge;
//     alert('the younger one is exactly half the age of the other in the year ' + dateHalf);
// } else {
//     differenceAge = dateSecond - dateFirst;
//     let dateHalf = dateSecond + differenceAge;
//     alert('the younger one is exactly half the age of the other in the year ' + dateHalf);   
// }

//Ex2
let zipCode = prompt ('enter your zip code, please: (5 digits only not more, no space)');

// let patt = new RegExp("d{5}");
// let res = patt.test(zipCode);

let res = /\d{5}/.test(zipCode);

alert(res);

if (res == true){
    alert('Your zipcode has the good format');
}else {
    alert('Your zipcode has a wrong format');
}

// //Ex3
// let word = prompt ('enter a word');

// const regex = /aeiou/i;
// console.log(word.replace(regex, ''));

// https://regex101.com/
// https://stackoverflow.com/questions/50813606/how-to-disallow-consecutive-five-digits-and-more-using-regex
// https://stackoverflow.com/questions/9011524/regex-to-check-whether-a-string-contains-only-numbers
// https://stackoverflow.com/questions/22082054/regex-to-match-if-no-space-is-found
// https://www.regextester.com/110149