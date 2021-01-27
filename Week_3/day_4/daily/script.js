let inputHtml = document.getElementById("fname");
let charValue = inputHtml.value;
inputHtml.addEventListener("keypress", myFunction);

function myFunction(event){
    //event.preventDefault();
    if (!isCharALetter(event.value)){
        console.log("not a letter");
    }
}

function isCharALetter (char){
    if (char>=65 && char<=90 || char>=97 && char<=122){
        return true;
    }else{
        return false;
    }
}