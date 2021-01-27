
function allowDropThis(event) {
	event.preventDefault(); // Necessary. Allows us to drop.
}
  
function dragThis(event) {
  event.dataTransfer.setData("text", event.target.id);
  console.log(event.dataTransfer);
}
  
function dropThis(event) {
  event.preventDefault();
  let data = event.dataTransfer.getData("text");
console.log(data);
//console.log(event.target);
event.target.appendChild(document.getElementById(data));
 // console.log(event.target.appendChild(document.getElementById(data)));
}








// function allowDropThis(i) {
//     i.preventDefault();
// }

// function dragThis(i) {
//     i.dataTransfer.setData("doggo", i.target.id);
// }

// function dropThis(i) {
//     i.preventDefault();
//     var data = i.dataTransfer.getData("doggo");
//     i.target.appendChild(document.getElementById(data));
// }