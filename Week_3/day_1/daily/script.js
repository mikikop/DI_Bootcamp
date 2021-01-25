//1
let planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"];
let colors = ["red","green","blue","yellow","grey","white","pink","orange","brown"];

//2 and 3 and 4
let bodyVar = document.body;
for (let i=0;i<planets.length;i++) {
    let divPlanet = document.createElement('div');
    let newTextNode = document.createTextNode(planets[i]);
    divPlanet.appendChild(newTextNode);
    divPlanet.classList.add("planet",planets[i].toLowerCase());
    divPlanet.style.background=colors[i];
    bodyVar.appendChild(divPlanet);
}

//Bonus

let moonsEarth = ["Moon"];
let moonsMars = ["Phobos","Deimos"];
let moonsJupiter = ["Io","Europa","Ganymede","Callisto"];
let moonsSaturn = ["Mimas","Enceladus","Tethys","Dione","Rhea","Titan","Hyperion","Iapetus","Phoebe"];
let moonsUranus = ["Puck","Miranda","Ariel","Umbriel","Titania","Oberon"];
let moonsNeptune = ["Proteus","Triton","Nereid"];
let moonsPluto = ["Charon"];

let moons = [moonsEarth,moonsMars,moonsJupiter,moonsSaturn,moonsUranus,moonsNeptune,moonsPluto];

for(let j=0;j<moons.length;j++){
    for(let i=0;i<moons[j].length;i++){
        let divMoon = document.createElement('div');
        divMoon.style.left = `${i*50+150}px`;
        let newTextNode = document.createTextNode(moons[j][i]);
        divMoon.appendChild(newTextNode);
        divMoon.classList.add("moon");
        bodyVar.children[j+3].appendChild(divMoon);
    }
}
