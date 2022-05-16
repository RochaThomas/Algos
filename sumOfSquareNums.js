//morning algos
//sum of square numbers

function sumOfSquareNums(num){
    for (let i = 1; i < Math.sqrt(num); i++){
        for (let j = i; j < Math.sqrt(num); j++){
            if (Math.pow(j, 2) + Math.pow(i, 2) === num){
                return true;
            }
        }
    }
    return false;
}

// console.log("Testing working num like 90000000000");
// console.log(sumOfSquareNums(90000000000));

// console.log("Testing non working num like 3");
// console.log(sumOfSquareNums(3));

//cool double var single loop solution

function sumOfSquareNumsEfficient(num){
    let start = 1;
    let end = Math.sqrt(num);
    while (start < end){
        if (Math.pow(start, 2) + Math.pow(end, 2) === num){
            return true;
        }
        else if (Math.pow(start, 2) + Math.pow(end, 2) > num){
            end--;
        }
        else {
            start++;
        }
    }
    return false;
}

console.log("Testing working num like 90000000000");
console.log(sumOfSquareNumsEfficient(90000000000));