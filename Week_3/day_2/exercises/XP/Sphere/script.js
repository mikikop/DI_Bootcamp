//to get the radius

let btnForm = document.getElementById("submit");
btnForm.addEventListener("click",volumeSphere);

function volumeSphere(event) {
    event.preventDefault();
    let radiusInput = document.getElementById("radius");
    let radiusValue = radiusInput.value;
    if(isNaN(radiusValue)){
        radiusInput.value = null;
        //radiusInput.style.borderColor = "red";
        radiusInput.style.border = "2px solid red";
        radiusInput.value = "only numbers are accepted"; 
    }else {
        let formula = (4/3) * Math.PI * Math.pow(radiusValue,3);
        let volumeInput = document.getElementById("volume");
        volumeInput.value = formula;
    }   
}


//append the formula to the input
//innerHTML, textContent, innnerText : NOT POSSIBLE
//value can be used with inputs

//if the value is a number so :OK
// if the value is a string delete whatever is in input and red borders to the input
//with message : only numbers are accepted