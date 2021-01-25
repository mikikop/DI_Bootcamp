//Ex2
//1
function getBold_items() {
    let boldItems = document.querySelectorAll("p > strong");
    return boldItems;
    //console.log(boldItems);
}

//2
function highlight() {
    let items = getBold_items();
    for (const iterator of items) {
        iterator.style.color = "blue";
    }
}

//3
function return_normal() {
    let items = getBold_items();
    for (const iterator of items) {
        iterator.style.color = "black";
    }
}

//4
let parHtml = document.querySelector("p");
parHtml.addEventListener("mouseover",highlight);
parHtml.addEventListener("mouseout",return_normal);