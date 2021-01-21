let hiddenWord;
let tabLetters = hiddenWord.split("");
let wordLength = hiddenWord.length;
let tabRes = [];
let lives = 10;
let incorrectLetters = [];

//fill the stars
for (i = 0; i < wordLength; i++) {
    tabRes[i] = "*";
}

console.log("tabletters: " + tabLetters);
console.log("size word " + wordLength);
console.log("tabres " + tabRes);

function checkTheLetter(letter) {
    for (const key in tabLetters) {
        if (Object.hasOwnProperty.call(tabLetters, key)) {
            const element = tabLetters[key];
            if (letter === element) {
                tabRes[key] = element;
                return true;
            } else {
                lifes -= 1;
                incorrectLetters[key].push(letter);
                return false;
            }
        }
    }
}

function endGame() {
    if (lives == 0) {
        return `Your dead hangman !`;
    } else if (!tabRes.includes("*")) {
        return `You win !`
    }
}


function letsPlay() {
    hiddenWord = prompt("Please enter a word to discover with at least 8 letters");
    do {
        let proposition = prompt(`Player 2: please choose a letter till you find the word ! you have still ${lives} lives.`);
        if (checkTheLetter(proposition) == true 
        

    } while (lives > 0 ||!tabRes.includes("*"))    


}

