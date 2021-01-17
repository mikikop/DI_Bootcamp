let sentence1 = "I am finding Nemo !";
let sentence2 = "I don't know where this fish is !";
let sentence3 = "It is a very strange exercise to find Nemo !";
let mySentences = [sentence1, sentence2, sentence3];

let goodAnswers = [4, 0, 9];

let firstAnswer = window.confirm("We'll display you a sentence and in few seconds you have to enter at which order the word \"Nemo\" is. This word could not be in the sentence then enter 0. Are you ready to play? ");

if (firstAnswer == false) {
    alert("You are not ready. Maybe another time !")
} else {
    const random = Math.floor(Math.random() * mySentences.length);
    theSentence = mySentences[random];
    let myAnswer = prompt(theSentence);
    if ((theSentence == mySentences[0] && myAnswer == goodAnswers[0]) || (theSentence == mySentences[2] && myAnswer == goodAnswers[2])) {
        alert("You found Nemo at " + myAnswer);
    } else if ((theSentence == mySentences[1] && myAnswer == goodAnswers[1])) {
        alert("You're right ! You can't find Nemo in this sentence");
    }else {
        alert("You lose !");
    }
}