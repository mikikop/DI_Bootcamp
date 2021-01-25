let libButton = document.getElementById('lib-button');
let libIt = function (event) {
    event.preventDefault();
    let nounInput = document.getElementById("noun").value;
    console.log(nounInput);

    let adjectiveInput = document.getElementById("adjective").value;
    //let adjectiveInputValue = adjectiveInput.value;
    //adjectiveInput.style.color = "red";
    console.log(adjectiveInput);

    let personInput = document.getElementById("person").value;
    console.log(personInput);
    
    let storyDiv = document.getElementById("story");
    storyDiv.innerHTML = `${personInput} was thinking about the ${nounInput} when a ${adjectiveInput} policeman asked to see the papers `;
};
libButton.addEventListener('click', libIt);