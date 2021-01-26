let libButton = document.getElementById('lib-button');
let libIt = function (event) {
    event.preventDefault();
    let nounInput = document.getElementById("noun").value;
    console.log(nounInput);

    let adjectiveInput = document.getElementById("adjective").value;
    console.log(adjectiveInput);

    let personInput = document.getElementById("person").value;
    console.log(personInput);
    
    let storyDiv = document.getElementById("story");
    storyDiv.innerHTML = `<span>${personInput}</span> was thinking about the <span>${nounInput}</span> when a <span>${adjectiveInput}</span> policeman asked to see the papers `;
    
    let spanAll =document.querySelectorAll("span");
    for (i=0;i<spanAll.length;i++){
        document.getElementsByTagName("span")[i].style.color ="red";
    }
};

libButton.addEventListener('click', libIt);