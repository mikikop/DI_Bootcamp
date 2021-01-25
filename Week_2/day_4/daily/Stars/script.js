let words = prompt("Please enter words separated by commas:");
let wordsArray = words.split(",");
let longestWord = 0;
// new frame with flame or heart emojis
const flame = String.fromCodePoint(0x1F525); 
const heart = String.fromCodePoint(0x2764);

// Create the FOR loop to find the longest word
for(let i = 0; i < wordsArray.length; i++){
    if(wordsArray[i].length > longestWord){ 
        longestWord = wordsArray[i].length;
     }
}

// create the line of stars above and under the frame
function wrapStars (longWord){
    //let stringStar = `*`.repeat(longWord+4);
    //let stringStar = `${flame}`.repeat(longWord+4);
    let stringStar = `${heart}`.repeat(longWord+4);
    return stringStar;
}

//create the spaces and star on the right
//number of space is composed by the size of longest world +4 chars - the length of the word 
// - 2 spaces of the left side - the star of the right side
function addRightStars(tab){
    for (i=0;i<tab.length;i++) {
        let numSpace = (longestWord+4)-(tab[i].length)-2-1;
        //tab[i] = tab[i] + " ".repeat(numSpace) + "*";
        //tab[i] = tab[i] + " ".repeat(numSpace) + `${flame}`;
        tab[i] = tab[i] + " ".repeat(numSpace) + `${heart}`;
    }
    return tab;
}


//create the star and space on the left 
function addLeftStars(tab){
    for (i=0;i<tab.length;i++) {
        //tab[i] = `* ` + tab[i];
        //tab[i] = `${flame}` + tab[i];
        tab[i] = `${heart}` + tab[i];
    }
    return tab;
}

addRightStars(wordsArray);
addLeftStars(wordsArray);
let starsLine = wrapStars(longestWord);

console.log(starsLine);
for (const key in wordsArray) {
    if (Object.hasOwnProperty.call(wordsArray, key)) {
        const element = wordsArray[key];
        console.log (`${element}` + '\n');
    }
}
console.log(starsLine);