let answer = prompt('How many lines of stars do you want?');
let starLine = Number(answer);

let tabStar = [];

//number of lines
for (let i = 0; i < starLine ; i++) {
  var starString = '';
  //number of stars per line
  for (let j=0; j<= i ; j++){
    starString = starString + '*'.repeat(j+1);
  }
  tabStar[i] = starString;
}

for (let i=0;i<tabStar.length;i++){
  console.log(" ".repeat(tabStar.length-i-1) + tabStar[i]+ " ".repeat(tabStar.length-i-1) + '\n');
}