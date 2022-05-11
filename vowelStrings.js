

function countStrings(n){
    let a = 1;
    let e = 1;
    let i = 1;
    let o = 1;
    let u = 1;

    while (n > 1){
        o += u;
        i += o;
        e += i;
        a += e;
        n--;
    }

    return a+e+i+o+u;
}

console.log(countStrings(1));
console.log(countStrings(2));
console.log(countStrings(3));
console.log(countStrings(4));
console.log(countStrings(5));
console.log(countStrings(6));
console.log(countStrings(7));