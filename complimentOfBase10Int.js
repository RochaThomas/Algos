//morning algos
//compliment of base ten integer

function compOfBaseTenInt(num){
    let binRep = num.toString(2);
    let compBinRep = "";

    for (let i = 0; i < binRep.length; i++){
        if (binRep[i] === "1"){
            compBinRep += "0";
        }
        else {
            compBinRep += "1";
        }
    }

    return parseInt(compBinRep, 2);
}

console.log(compOfBaseTenInt(10));