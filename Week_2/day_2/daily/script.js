// let sentence = 'this dinner is not bad !';
// let sentence = 'This movie is not so bad!';
// let sentence = 'this dinner is bad !';
let sentence = 'this dinner is not so bad, but it\'s cool !';

//first not occurence index
let notFirstOcc = sentence.indexOf('not');
let badFirstOcc = sentence.indexOf('bad');

//test
if (notFirstOcc == -1 || badFirstOcc == -1 || notFirstOcc > badFirstOcc) {
    alert(sentence);
} else if (notFirstOcc < badFirstOcc) {
    let newSentence = sentence.substr(0, notFirstOcc - 1);
    let endSentence = sentence.substr(badFirstOcc+3,sentence.length);
    if (endSentence == null) {
        alert(newSentence + ' good ');
    } else {
        alert(newSentence + ' good' + endSentence);
    }
    
}