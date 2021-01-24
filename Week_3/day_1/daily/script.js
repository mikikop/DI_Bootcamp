//1
let planets = ["Mercury","Venus","Earth","Mars","Jupiter","Saturn","Uranus","Neptune","Pluto"];

//2 and 3 and 4
let bodyVar = document.body;
for (const iterator of planets) {
    let divPlanet = document.createElement('div');
    let newTextNode = document.createTextNode(iterator);
    divPlanet.appendChild(newTextNode);
    bodyVar.appendChild(divPlanet);
    divPlanet.classList.add("planet",iterator);
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
        let divMoon ;
        divMoon = document.createElement('div');
        let newTextNode = document.createTextNode(moons[j][i]);
        divMoon.appendChild(newTextNode);
        divMoon.classList.add("moon");
        bodyVar.children[j+3].appendChild(divMoon);
    }
}
