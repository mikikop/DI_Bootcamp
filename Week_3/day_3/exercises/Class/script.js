// console.log("Before set timeout");

// function sayHi(message) {
// 	let container = document.getElementById("container");
// 	container.textContent = message;
// 	container.style.backgroundColor = "yellow";
// }

// setTimeout(sayHi,2000,"Your cart is empty");

// //This instruction will be executed even if the setTimeout is still not executed
// console.log("After set timeout");

//EX1
// function banner(message) {
// 	let container = document.getElementById("container");
// 	container.style.visibility = "visible";
// }

// setTimeout(banner,5000);

//setInterval allows to repeat a function with an interval of time
//setInterval(banner, 2000);
// let bye = document.getElementById("containerBye")
// ​
// //set the setinterval : the interval is called "timing"
// let timing = setInterval(sayHi, 2000);
// ​
// bye.addEventListener("click", stopTimer)
// ​
// function sayHi() {
// 	console.log("console.log in setinterval")   
// }
// ​
// function stopTimer(){
// 	//stop the interval called "timing"
// 	clearInterval(timing)
// }



//Ex2
let timing = setInterval(countdown,1000);
let x = 10;

function countdown(){
	let container = document.getElementById("container");
	container.textContent = `The sales end in ${x} sec !`
	if(x == 0){
		clearInterval(timing);
	}else{
		container.style.visibility = "visible";
	}
	x--;
}


