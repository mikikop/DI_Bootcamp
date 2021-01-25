//Ex1
//1
let parAll = document.querySelectorAll('article > p');
console.log(parAll);
for (let i = 0; i < parAll.length; i++) {
    parAll[i].classList.add("para_article");
}

//2
// let parLast = parAll[parAll.length - 1];
// parLast.remove();

//3
let h2 = document.querySelector('h2');
h2.addEventListener('click', removeFunc);

function removeFunc(event) {
    event.target.remove();
}

//4
let h1 = document.querySelector('h1');
h1.addEventListener('click', fontRandom);

function fontRandom(event) {
    let fontSize = Math.floor(Math.random() * 100);
    event.target.style.fontSize = fontSize + "px";
}

//5
let parFirst = parAll[0];
parFirst.addEventListener('click', hidePar);

function hidePar(event) {
    event.target.style.display = "none";
}

//6
let inputHTML = document.querySelectorAll('input');
console.log(inputHTML);

let table = document.createElement('table');
let thead = table.createTHead();
let row = thead.insertRow(0);
let cell = row.insertCell(0);
cell.innerHTML = "<b> my name</b>";
let row1 = thead.insertRow(1);
let cell1 = row.insertCell(1);
cell1.innerHTML = "<b> my thoughts</b>";
document.body.appendChild(table);

inputHTML[0].addEventListener("change", insertTable);
inputHTML[1].addEventListener("change", insertTable);

let tr = document.createElement('tr');


function insertTable(event) { 
    
    var td = document.createElement('td');
        td.appendChild(document.createTextNode(event.target.value));
        tr.appendChild(td);
        table.appendChild(tr);
}

//7
let secondPar = parAll[1];
secondPar.addEventListener("click", fadeOut);

function fadeOut(event) {
event.classList.add('hide');
}

