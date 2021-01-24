// //Ex1
// let bodyVar = document.body;
// let divVar = bodyVar.firstElementChild;


// //1
//  divVar.setAttribute("id","socialNetworkNavigation");

//  //2
//  //2.1
//  let newLi = document.createElement("li");

// //2.2
// let newTextNode = document.createTextNode('Logout');

// //2.3
// newLi.appendChild(newTextNode);

// //2.4
// let ulVar = divVar.firstElementChild;
// ulVar.appendChild(newLi);

// //Bonus
// let firstLi = ulVar.firstElementChild;
// let firstAtag = firstLi.firstElementChild;
// console.log(firstAtag.children[0].nodeValue);

// let lastLi = ulVar.lastElementChild;
// console.log(lastLi.children[0].nodeValue);



// //EX2
// let bodyVar = document.body;
// let firstUlVar = bodyVar.children[1];

// //1
// firstUlVar.children[1].textContent = "Richard";

// //2
// let itemClass = document.getElementsByClassName("list");
// for(i=0;i<itemClass.length;i++){
//     itemClass[i].getElementsByTagName("li")[0].textContent = "Michael";
// }

// //3
// let allUl = document.getElementsByTagName("ul");
// for (let selectedUl of allUl) {
//     let newLi = document.createElement("li");
//     let newTextNode = document.createTextNode('Hey students');
//     newLi.appendChild(newTextNode);
//     selectedUl.appendChild(newLi);
// }

// //4
// let liFive = document.getElementsByTagName("li")[4];
// let secondUl = document.getElementsByTagName("ul")[1];
// secondUl.removeChild(liFive);

// //Bonus1
// for (let selectedUl of allUl) {
//     selectedUl.setAttribute("class", "student_list");
// }

// //Bonus2
// firstUlVar.classList.add("university");
// firstUlVar.classList.add("attendance");


//Ex3
//on github


//Ex4
let bodyVar = document.body;
let firstDiv = bodyVar.firstElementChild;
let firstUl = firstDiv.nextElementSibling;

 //1
 firstDiv.style.background = "lightblue";
 firstDiv.style.padding = "10px";

 //2
 firstUl.firstElementChild.style.display = "none";
 firstUl.children[1].style.border = "2px solid black";

 //3
 bodyVar.style.fontSize = "x-large";

 //Bonus
 let userX =firstUl.children[0].textContent;
 let userY =firstUl.children[1].textContent;
 if (firstDiv.style.background == "lightblue"){
     alert(`Hello ${userX} and ${userY}`);
 }
