//1
function insert_Row() {
	let tableVar = document.getElementById("sampleTable");
	let tabRows = tableVar.rows.length;
	let newRow = document.createElement("tr");
	for(let i=0; i<2;i++){
		let newCol = document.createElement("td");
		let newTextNode = document.createTextNode(`Row${tabRows+1} Cell${i+1}`);
		newCol.appendChild(newTextNode);
		newRow.appendChild(newCol);
	}
	tableVar.appendChild(newRow);
}


//2
let btn = document.getElementById('jsstyle');
btn.addEventListener("click",changeText);
btn.addEventListener("mouseover",changeColor);

function changeText(event) {
	// all the properties of the event object
	console.log("event", event) ;
	console.log("My mouse is over the btn named " + event.target.innerHTML);
    console.log("event.type: ", event.type);
	event.target.innerHTML = "Hello";
}

function changeColor(event) {
	event.target.style.backgroundColor = "red";
	console.log(event.target);
}