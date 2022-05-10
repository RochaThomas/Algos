
function singleNumber(arr){

    let numDict = {};
    for (let i = 0; i < arr.length; i++){
        if (numDict[arr[i]]){
            numDict[arr[i]] += 1;
        }
        else {
            numDict[arr[i]] = 1;
        }
    }

    for (const num in numDict){
        if (numDict[num] < 2){
            return num;
        }
    }

    return null;

}

const testingArr = [1,2,3,4,5,1,2,3,4];

console.log("Testing Single Number, should print 5");
console.log(singleNumber(testingArr));
