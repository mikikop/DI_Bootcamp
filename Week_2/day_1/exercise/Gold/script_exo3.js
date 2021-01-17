let str1 = 'mix';
let str2 = 'pod';
console.log("#1 "+str1 +" #2 "+str2);

//take the first two letters of each string and assign to a new variable
let str1_twoLetters = str1.substr(0,2);
let str2_twoLetters = str2.substr(0,2);
console.log("#1 "+str1_twoLetters +" #2 "+str2_twoLetters);

//extract a part of each string - without the first letter
str1 = str1.substr(2,1);
str2 = str2.substr(2,1);
console.log("#1 "+str1 +" #2 "+str2);

//concat the first letter of str1 with the extract of str2 and the first letter of str2 with the extract of str1
str1 = str2_twoLetters + str1;
str2 = str1_twoLetters + str2;
console.log("#1 "+str1 +" #2 "+str2);

//result
let newWord = str1 + " " +str2;
console.log(newWord);