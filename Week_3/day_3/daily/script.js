let inputHtml = document.getElementById("fname");
//let charValue = inputHtml.value;
console.log(inputHtml.textContent);
inputHtml.addEventListener("keypress", myFunction);

function myFunction(event){
    //event.preventDefault();
    if (!isCharALetter(inputHtml.textContent)){
        console.log("not a letter");
    }
}

function isCharALetter (char){
    return (/[a-zA-Z]/.test(char));
}