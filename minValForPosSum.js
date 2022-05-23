//morning algos
//minimum value to get positive step by step sum


function minValForPosSum(nums){
    let isPos = false;
    let startVal = 1;
    while (isPos === false){
        let copyVal = startVal;
        for (let i = 0; i < nums.length; i++){
            copyVal += nums[i];
            if (copyVal < 1){
                break;
            }
        }
        if (copyVal >= 1){
            return startVal;
        }
        startVal++;
    }
    return "broken";
}
//^^ this works but lets make it "better"...

function fasterSol(nums){
    let minAdd = 0;
    let sum = 0;
    for (let i = 0; i < nums.length; i++){
        sum += nums[i];
        if (sum < minAdd){
            minAdd = sum;
        }
    }
    return Math.abs(minAdd) + 1;
}

// console.log("Testing slow solution...");
// console.log(minValForPosSum([-8,7,-10,6,4,-9]));

console.log("Testing better solution...");
console.log(fasterSol([-8,7,-10,6,4,-9]));