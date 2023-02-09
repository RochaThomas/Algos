# cracking the coding interview 
# chapter 5 bit manipulation

# interview questions

# 5.1 insertion
# given 2 32-bit numbers, m and n, and two bit positions, i and j. write a function that inserts n into m
# such that m starts at j and ends at i
def insertion(m, n, i, j):
    """
    clear bits from i to j
    shift n to the left to line up with i and j
    return m | n
    """
    frontMask = (-1 << (j + 1))
    backMask = (1 << i)
    mask = frontMask | backMask
    m = m | mask
    n = n << (j + 1)

    return m | n

# 5.2 binary to string
# print the binary respresentation of a real number between 1 and 0 oassed as a double
def binaryToString(d):
    """
    hard to understand by reading but makes a lot of sense if you read then go through a test case
    bits are base 2, when its a base 10 num you shift digits left by multiplying by 10
    for bits you shift the number to the left by multiplying by 2
    if you multiple decimal by 2 and num is greater than 1 then a 1 goes in that place in a bitwise manner
    d = 0.71
        d x 2 = 1.41
            res = .1 <- 1 is appended to answer because d > 1
            then d -= 1, d = .41
        d x 2 = .82
            res = .10 <- 0 is appended because d < 1
        d x 2 = 1.64
            res = .101
            d = .64
        d x 2 = 1.28
            res = .1011
            d = .28
        etc
    """
    if d >= 1 or d <= 0:
        return "ERROR"
    res = "."
    while d > 0:
        if len(res) > 32:
            return "ERROR"
        
        newD = d * 2
        if newD >= 1:
            res.append("1")
            newD -= 1
        else:
            res.append("0")
    return res

# 5.3 flip bit to win
# given an integer and the ability to flip exactly 1 bit from 0 to 1, write an algorithm that will flip 1 bit to return the longest
# sequence of 1s you can create
def flipBitToWin(num):
    """
    one way is to get the num in 32 bit representation
    iterate through the bits keeping track of the lengths of sequences of 0s and 1s pushing it to an array
    the array will have counts of alternating sequences 0s and 1s
    if the length of the 0 sequence is 1 then the count of the sequences before and after the 0 sequence can be added and compared
    to the max length

    another way to do it is in place with no extra memory and same O(b) run time
    keep track of previous length and current length
    if current bit is 1 current length += 1
    else (current bit is 0)
        check is next bit is 1 or 0
        if 0 then previous length is 0
        if 1 then previous length is current length
        reset current length to 0 regardless (once you hit a 0 current length ends)
    after the end of the if else block
        compare currentLength + previousLength + 1 to maxLength
    """
    if ~num == 0: return 32
    currentLength, previousLength = 0, 0
    maxLength = 1

    while num != 0:
        if num & 1 == 1:
            currentLength += 1
        elif num & 1 == 0:
            previousLength == 0 if num & 2 == 0 else currentLength
            currentLength = 0
        maxLength = max(maxLength, previousLength + currentLength + 1)
        
        # this last line may mess up the algorithm because python only has arithmetic shifts  >>
        # java on the other hand has both arithmetic >> and logical >>>
        # for this algo this next line should be >>> but we don't have that in python
        #   may need a helper function
        num >>= 1
    return maxLength

# 5.4 next number
# given a positive integer, print the next smallest and next largest numbers that have the same number of 1 bits
# in their binary representation
def nextNumber(num):
    pass
