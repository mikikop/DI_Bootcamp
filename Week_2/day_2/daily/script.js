// let sentence = 'this dinner is not bad !';
// let sentence = 'This movie is not so bad!';
let sentence = 'this dinner is bad !';

//first not occurence index
let notFirstOcc = sentence.indexOf('not');
let badFirstOcc = sentence.indexOf('bad');

//test
if (notFirstOcc == -1 || badFirstOcc == -1 || notFirstOcc > badFirstOcc) {
    alert(sentence);
} else if (notFirstOcc < badFirstOcc) {
    let newSentence = sentence.substr(0, notFirstOcc - 1);
    alert(newSentence + ' good !');
}