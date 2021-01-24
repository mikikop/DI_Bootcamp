//1
let bodyVar = document.body;
let divVar = bodyVar.firstElementChild;
             //bodyVar.children[0];
 
//2 : UL IS NOT A CHILD OF THE DIV
let ulVar = bodyVar.children[1]
            //divVar.nextElementSibling;

//3
let liSecondVar = ulVar.children[1];
                //ulVar.lastElementChild;



//How to change the text content of the 3rd li to "John"
​
//get the body
let bodyWebsite = document.body
//get the div
let divWebsite = bodyWebsite.firstElementChild
				//bodyWebsite.children[0]
//get the ul
let ulWebsite = divWebsite.firstElementChild
//get the li
let liThirdWebsite = ulWebsite.lastElementChild
console.log(liWebsite)
​
//change the text node of the li
liThirdWebsite.textContent = "John"
​
//get the second li of the ul
let liSecondWebsite = liThirdWebsite.previousElementSibling
console.log("Second li : ", liSecondWebsite)
​
//get the parent of the li
console.log("parent of li: ", liSecondWebsite.parentNode)



let bodyWebsite = document.body
let newDiv = document.createElement("div")
​
for (let i = 0; i < 5; i++){
	let newImage = document.createElement("img")
	newImage.setAttribute("src", "cat.jpg")
	let newParagraph = document.createElement("p")
	newParagraph.className = "welcomeUser"
	let newContent = document.createTextNode("Hello new users " + i)
	newParagraph.appendChild(newContent)
	newDiv.appendChild(newParagraph)
	newDiv.appendChild(newImage)
}
​
bodyWebsite.appendChild(newDiv)