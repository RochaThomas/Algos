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
    pass