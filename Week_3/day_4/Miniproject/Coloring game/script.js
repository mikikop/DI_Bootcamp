let numPalette = 3*7;
let paletteColor = ["#FC1D00","#FC4401","#FDA500","#FFFF01","#9ACD32","#90EE90","#177F00","#40E0D0","#2EFDFF","#87CEFA","#1E90FF","#0000FF","#00008B","#4B0082","#8B048B","#EE82EE","#FDB6C1","#D3D3D3","#808080","#000000","#FFFFFF"];
let numGrid = 60*24;
let gridColor = ["FFFFFF"];
let contPaletteId = document.getElementById("sidebar");
let contGridId = document.getElementById("sidegrid");
let colorSelected;
let clearButton;
let tabColored = [];
let isReleased = false;

//add divs to the html
function addDiv(num,className,id) {
	let divContainer = id;
	//console.log(divContainer);
	for(i=1;i<=num;i++){
		let newDiv = document.createElement("div");
		newDiv.classList.add(className);
		divContainer.appendChild(newDiv);
	}
}

//add palette divs and grid divs
addDiv(numPalette,"palette",contPaletteId);
addDiv(numGrid,"grid",contGridId);

//select all the divs with class palette
let divPalette = document.querySelectorAll(".palette");

//select all the divs with class grid
let divGrid =document.querySelectorAll(".grid");

//both function to fill a background color
function fillPaletteBackgroundColor(divArray,colorArray) {
	for(let i=0; i<divArray.length; i++){
		divArray[i].style.backgroundColor = `${colorArray[i]}`;
	}
}

function fillGridBackgroundColor(divArray) {
	for(let i=0; i<divArray.length; i++){
		//console.log(divArray[i]);
		divArray[i].style.backgroundColor = "#FFFFFF";
	}
}

//fill the background color of the palette divs
fillPaletteBackgroundColor(divPalette,paletteColor);
//fill the background color of the grid divs
fillGridBackgroundColor(divGrid);

//add a listener
function addListener(collection, event, myFunction) {
	for(let i=0;i<collection.length;i++){
		collection[i].addEventListener(event,myFunction);
	}
}

//add a listener to the pallette by clicking
addListener(divPalette,"click",selectAColor);

//add a listener to the grid by mousedown to put isReleased to true and to color by clicking
addListener(divGrid,"mousedown",released);
addListener(divGrid,"mousedown",dropAColor);

//add a listener to the grid by mouseover only when isReleased is true
addListener(divGrid,"mouseover",dropAColor);

//add a listener to the grid by mouseup to put isReleased to false
addListener(divGrid,"mouseup",notReleased);

//add a listener to the clear button
clearButton = document.getElementById("clearMe");
clearButton.addEventListener("click",clear);

//select a color on the palette
function selectAColor(event) {
	colorSelected = event.target.style.backgroundColor;
}

//drop a color and store in an array the colored div
function dropAColor(event) {

	if(isReleased){
	
		event.target.style.backgroundColor = colorSelected;
		tabColored.push(event.target);
	}
	
}

function released(event) {
	isReleased = true;
}

function notReleased(event) {
		isReleased = false;
}


//clear only the colored div
function clear(event) {
	for(let i=0;i<tabColored.length;i++){
		tabColored[i].style.backgroundColor = "#FFFFFF";
	}
}
