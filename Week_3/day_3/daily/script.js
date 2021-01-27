let inputHtml = document.forms[0].children[2];
inputHtml.addEventListener("keyup", myFunction);

function myFunction(event){
    let str = inputHtml.value;
    if (!isCharALetter(event.keyCode)){
        console.log("not a letter");
        inputHtml.value = str.slice(0,-1);
    }
}

function isCharALetter (char){
    if (char>=65 && char<=90 || char>=97 && char<=122){
        return true;
    }else{
        return false;
    }
}

//Igor solution
// var volume = document.forms[0].children[0];
//         volume.onkeyup = function (event) {
//             var str = volume.value;
//             var x = event.keyCode;
//             if (x < 65 || x > 122 || (x > 90 && x < 97)) {
//                 volume.value = str.slice(0, -1);
//             }
//         };