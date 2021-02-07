let arrayVaccineIsrael = [{
	type: "Covid-19",
	qty: "1000"
}];

let arrayPerson = [{
	id: "319247332",
	name: "Michael Perez",
	numVac: 0,
},
{
	id: "234568145",
	name: "Elina Levi",
	numVac: 1,
},
{
	id: "114900645",
	name: "Nativ Cohen",
	numVac: 0,
}];

let arrayKupa = [{
	id: 1,
	name: "macabi",
	location: "raanana",
	address: "Ben gurion 24, Raanana, Israel",
	stockStart: 100,
	stockUpdate: 100
},
{
	id: 2,
	name: "macabi",
	location: "raanana",
	address: "Ahuza 124, Raanana, Israel",
	stockStart: 233,
	stockUpdate: 233
},
{
	id: 3,
	name: "macabi",
	location: "tel aviv",
	address: "Levi Eshkol 26, Tel Aviv, Israel",
	stockStart: 50,
	stockUpdate: 40
},
{
	id: 4,
	name: "clalit",
	location: "raanana",
	address: "Kazan Street 14, Raanana, Israel",
	stockStart: 127,
	stockUpdate: 12
},
{
	id: 5,
	name: "clalit",
	location: "tel aviv",
	address: "Mapu 3, Tel Aviv, Israel",
	stockStart: 200,
	stockUpdate: 11
}];

let cells = ["NAME", "ID", "VACCINE", "DATE", "STATUS"];
let info = [];
//////////// HTML KUPA /////////
function retrievePerson() {
	// let getTable = document.getElementById("table");
	// getTable.remove();
	document.get
	let getId = document.getElementById("idnum").value;
	let idPerson = Number(getId);
	if (!Number.isInteger(idPerson || getId == "" || getId == " ")) {
		alert("You have to enter a ID number");
	} else {
		for (let i = 0; i < arrayPerson.length; i++) {
			if (arrayPerson[i].id == idPerson) {
				let nameUser = arrayPerson[i].name;
				let idUser = arrayPerson[i].id;
				let numVac = arrayPerson[i].numVac;

				let date = new Date();
				let day = date.getDate();
				let month = date.getMonth() + 1;
				let year = date.getFullYear();
				let myDate = `${day}/${month}/${year}`;

				info.push(nameUser);
				info.push(idUser);
				info.push(numVac);
				info.push(myDate);
			}
		}

		let table = document.createElement("table");
		table.setAttribute("id", "myTable");
		//START FOR LOOP i
		for (let i = 0; i < 2; i++) {
			let newRow = table.insertRow();
			//START FOR LOOP j
			for (let j = 0; j < 5; j++) {
				let newCell = newRow.insertCell();
				if (i == 0) {
					//NEW
					newCell.innerHTML = cells[j]
				} else {
					if (j == 4) {
						let btn = document.createElement("button");
						btn.addEventListener("click", vaccineDone);
						btn.innerText = "Done";
						btn.style.backgroundColor = "#4CAF50";
						newCell.appendChild(btn);
					} else {
						newCell.innerHTML = info[j]
					}
				}
				//NEW
				newRow.appendChild(newCell);
				//END FOR LOOP j
			}
			table.appendChild(newRow);
			//END FOR LOOP i
		}
		//NEW
		document.body.appendChild(table);
	}
}


function vaccineDone() {
	//retrieve the person
	let myId = document.getElementById("myTable").children[2].children[1].innerText;
	console.log(myId);
	//increment the numVacc in the person object
	for (const key in arrayPerson) {
		if (arrayPerson[key].id == myId) {
			arrayPerson[key].numVac += 1;
			console.log(arrayPerson[key].numVac);
		}
	}
	//display done
	let statusCell = document.getElementById("myTable").children[2].children[4];
	console.log(statusCell);
	statusCell.children[0].remove();
	statusCell.innerText = "Done";
	statusCell.style.color = "green";
	statusCell.style.fontWeight = "bold";

	//retrieve the id kupat holim
	let getIdKupa = document.getElementsByTagName("span")[0].id;

	//decrement the stockUpdate in the kupa object
	for (const key in arrayKupa) {
		if (arrayKupa[key].id == getIdKupa) {
			arrayKupa[key].stockUpdate -= 1;
			//if it's under 10 launch an alert
			if (arrayKupa[key].stockUpdate < 10) {
				alert(`Warning : It stays ${arrayKupa[key].stockUpdate} vaccines in stock`);
			}
		}
	}

	//update the cell of vaccine
	let vaccineCell = document.getElementById("myTable").children[2].children[2];
	console.log(vaccineCell);
	for (const key in arrayPerson) {
		if (arrayPerson[key].id == myId) {
			vaccineCell.innerText = arrayPerson[key].numVac;
		}
	}
}


///////////////////// HTML VISITOR ////////////////
let cellsKupa = ["NAME", "STOCK", "ADDRESS", "MAP"];
let infoKupa = [];


function findVaccine(event) {
	event.preventDefault();
	let tableKupa = document.createElement("table");
	
		let myCity = document.getElementById("categories").value;
		let myKupa = document.getElementById("search-field").value;
		let city = myCity.toLowerCase();
		let kupa = myKupa.toLowerCase();

		for (let i = 0; i < arrayKupa.length; i++) {
			if (arrayKupa[i].location == city && arrayKupa[i].name == kupa) {
				let idK = arrayKupa[i].id;
				let nameK = arrayKupa[i].name;
				let locationK = arrayKupa[i].location;
				let addressK = arrayKupa[i].address;
				let stockuK = arrayKupa[i].stockUpdate;

			
						infoKupa.push(idK);
						infoKupa.push(nameK);
						infoKupa.push(locationK);
						infoKupa.push(addressK);
						infoKupa.push(stockuK);
			
				
				

				console.log(`the kupa: ${myKupa} and the city ${myCity} has spot in 
			${arrayKupa[i].address} and it stays ${arrayKupa[i].stockUpdate} vaccines in stock`);
			console.log(infoKupa);
			}
			
			tableKupa.setAttribute("id", "visiTable");
			//START FOR LOOP i
			for (let i = 0; i < infoKupa.length; i++) {
				let newRow = tableKupa.insertRow();
				//START FOR LOOP j
				for (let j = 0; j < 4; j++) {
					let newCell = newRow.insertCell();
					if (i == 0) {
						newCell.innerHTML = cellsKupa[j]
					} else {
						if (j == 3) {
							let icone = document.createElement("i");
							icone.addEventListener("click", redirectMap);
							icone.classList.add("fas", "fa-map-marked");
							newCell.appendChild(icone);
						} else{
							newCell.innerHTML = infoKupa[j];
						}
					}
					newRow.appendChild(newCell);
					//END FOR LOOP j
				}
				tableKupa.appendChild(newRow);
				//END FOR LOOP i
			}
			document.body.appendChild(tableKupa);
		}
	
}

let addressUrl = ["https://goo.gl/maps/aaRXZ2KNgV8i7ecf8", "https://goo.gl/maps/xJzNbbw4uRoF6PCK9", "https://goo.gl/maps/m2szGtf4sqePLPAN6", "https://goo.gl/maps/swY4jTHxYyKMVUNK7", "https://goo.gl/maps/91atqRvF6ySrQm6B7"];
function redirectMap(event) {
	event.preventDefault();
	//retrieve the address


	if (address == "Ben gurion 24, Raanana, Israel") {
		var url = addressUrl[0];
		window.location(url);
	} else if (address == "Ahuza 124, Raanana, Israel") {
		var url = addressUrl[1];
		window.location(url);
	} else if (address == "Levi Eshkol 26, Tel Aviv, Israel") {
		var url = addressUrl[2];
		window.location(url);
	} else if (address == "Kazan Street 14, Raanana, Israel") {
		var url = addressUrl[3];
		window.location(url);
	} else if (address == "Mapu 3, Tel Aviv, Israel") {
		var url = addressUrl[4];
		window.location(url);
	} else {
		alert("This address is not found")
	}

}