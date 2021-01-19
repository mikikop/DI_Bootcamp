let answer = prompt('How many lines of stars do you want?');
let starLine = Number(answer);

let tabStar = [];


for (let i = 0; i < starLine ; i++) {
  var starString = '';
  for (let j=0; j<i+1 ; j++){
    starString = starString + '*';
  }
  tabStar[i] = starString;
}

for (let i=0;i<tabStar.length;i++){
  console.log( tabStar[i]+'\n');
}
