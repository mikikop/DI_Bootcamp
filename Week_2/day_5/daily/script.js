let x = 99;
let y = 1;

function couplet(xArg,yArg) {
    let tabCouplet = [];

    if (y == 1) {

        tabCouplet.push(`${xArg} bottles of beer on the wall \n`);
        tabCouplet.push(`${xArg} bottles of beer \n`);
        tabCouplet.push(`Take ${yArg} down, pass it around \n`);
        tabCouplet.push(`${xArg-yArg} bottles of beer on the wall \n`);
        return tabCouplet;
    }else {
        tabCouplet.push(`${xArg} bottles of beer on the wall \n`);
        tabCouplet.push(`${xArg} bottles of beer \n`);
        tabCouplet.push(`Take ${yArg} down, pass them around \n`);
        tabCouplet.push(`${xArg-yArg} bottles of beer on the wall \n`);
        return tabCouplet;
    }
  
}


do{
console.log(couplet(x,y).join(" "));
x=x-y;
y=y+1;

} while((x-y)>0);