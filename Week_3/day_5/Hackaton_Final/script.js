let startTime;
let elapsedTime = 0;
let timerInterval;

function timeToString(time){
    let hours = time/3600000;
    let hh = Math.floor(hours);

    let minutes = (hours - hh)*60;
    let mm = Math.floor(minutes);

    let seconds = (minutes - mm)*60;
    let ss = Math.floor(seconds);

    let millisec = (seconds - ss)*100;
    let ms = Math.floor(millisec);

    let formattedH = hh.toString().padStart(2,"0");
    let formattedM = mm.toString().padStart(2,"0");
    let formattedS = ss.toString().padStart(2,"0");
    let formattedMs = ms.toString().padStart(2,"0");

    return `${formattedM}:${formattedS}:${formattedMs}`;
}

function print (text){
    document.getElementById("display").innerHTML = text;
}

function start(){
    startTime = Date.now();
    timerInterval = setInterval(function printTime(){
        elapsedTime = Date.now() - startTime;
        print(timeToString(elapsedTime));
    }, 10);
    showButton("STOP");
}

function stop(){
    clearInterval(timerInterval);
    print("OO:00:00");
    elapsedTime = 0;
    showButton("PLAY");
    
}

function showButton(buttonKey) {
    const buttonToShow = buttonKey === "PLAY" ? playButton : stopButton;
    const buttonToHide = buttonKey === "PLAY" ? stopButton : playButton;
    buttonToHide.style.display = "none";
    buttonToShow.style.display = "block";
    let lanternes = document.getElementById("lanternes");
    let lanterne = 
}


let playButton = document.getElementById("playButton")
let stopButton = document.getElementById("stopButton")

playButton.addEventListener("click",start);
stopButton.addEventListener("click",stop);