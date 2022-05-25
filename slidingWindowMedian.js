//morning algos
//sliding window median

//unfinished this doesnt work...
function slidingWindowMedian(nums, k){
    let output = [];
    if (k % 2 === 0){
        const shift = k / 2 - 1;
        for (let i = shift; i < nums.length - shift - 1; i++){
            output.push((nums[i] + nums[i + 1]) / 2);
        }
    }
    else {
        const shift = Math.floor(k/2);
        for (let i = shift; i < nums.length - shift; i++){
            output.push(nums[i]);
        }
    }
    return output;
}

console.log(slidingWindowMedian([1,3,-1,-3,5,3,6,7], 3));