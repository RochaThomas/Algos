// testing for wordles with friends

const genSalt = () => {
    let salt = "";

    // generating a salt that is 6 characters or numbers long
    while (salt.length < 8){
        // random number generator to choose a number or a letter
        const letterOrNum = Math.round(Math.random());
        // if its 0 then letter if 1 then a number
        if (letterOrNum === 0){
            // random number generator to choose upper or lower case
            const upperOrLower = Math.round(Math.random());
            // get a random number corresponding to a random letter
            letterNum = Math.floor(Math.random() * 26);
            // create a var which will control upper or lower case conversion
            let caseAdder = null
            // set caseAdder based on random number
            // 0 -> upper -> 65
            if (upperOrLower === 0){
                caseAdder = 65
            }
            // 1 -> lower -> 97
            else {
                caseAdder = 97
            }
            // convert number to character and add it to the salt
            salt += String.fromCharCode(caseAdder + letterNum);
        }
        else {
            // generate random number 0-9 as a char
            const num = Math.floor(Math.random() * 10);
            salt += num
        }
    }

    return salt
}

console.log(genSalt());