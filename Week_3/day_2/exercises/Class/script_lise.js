//1
function clickParagraph() {
	console.log("hello")
	document.getElementById("p").classList.toggle("welcomeUser")
}

//2
document.getElementById("p").onclick = function () {
	console.log("hello")
	document.getElementById("p").classList.toggle("welcomeUser")
}


//3
let container = document.getElementById("container")
for (let i = 0; i<3; i++){
	let p = document.createElement("p")
	let content = document.createTextNode("Hello")
	p.appendChild(content)
	container.appendChild(p)
} 