
function romanToInt(roman){
    let output = 0;

    for (let i = 0; i < roman.length; i++) {
        switch(roman[i]){
            case 'M':
                output+= 1000;
                break;
            case 'D':
                output += 500;
                break;
            case 'C':
                if (roman[i+1] === 'M'){
                    output += 900;
                    i++;
                }
                else if (roman[i+1] === 'D'){
                    output += 400;
                    i++;
                }
                else {
                    output += 100;
                }
                break;
            case 'L':
                output += 50;
                break;
            case 'X':
                if (roman[i+1] === 'C'){
                    output += 90;
                    i++;
                }
                else if (roman[i+1] === 'L'){
                    output += 40;
                    i++;
                }
                else {
                    output += 10;
                }
                break;
            case 'V':
                output += 5;
                break;
            case 'I':
                if (roman[i+1] === 'X'){
                    output += 9;
                    i++;
                }
                else if (roman[i+1] === 'V'){
                    output += 4;
                    i++;
                }
                else {
                    output += 1;
                }
                break;
            default:
                output += 0;
                break;
        }
    }

    return output;
}

console.log("Testing converter DLXVII should be 567")
console.log(romanToInt("DLXVII"));

console.log();

console.log("Testing converter CDLXXXIX should be 489")
console.log(romanToInt("CDLXXXIX"));