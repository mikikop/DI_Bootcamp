let container = document.getElementById("container");
let animate = document.getElementById("animate");

container.appendChild(animate);
document.appendChild(container);

function myMove() {
	var pos =0;
	let id = setInterval(function () {
		if (pos == 350){
			clearInterval(id);
		}else{
			pos++;
			animate.style.left = pos + "px";
		}
	},5)
}