//morning algos
//maximum wealth

function maxWealth(arr){
    let max = 0;

    for (let i = 0; i < arr.length; i++){
        let sum = 0;
        for (let j = 0; j < arr[i].length; j++){
            sum += arr[i][j];
        }
        if (sum > max){
            max = sum;
        }
    }
    return max;
}

console.log(maxWealth([[1,2,3],[3,2,1]]));
console.log(maxWealth([[2,8,7],[7,1,3],[1,9,5]]));