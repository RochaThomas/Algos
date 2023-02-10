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
    """
    brute force is to get num as binary representation, and count 1s
    then increment or decrement num (count 1s) until you find the next num that matches the number of 1s

    flipping a 1 -> 0 and a 0 -> 1 at the same time keeps the same numbers of 1s
    if the 1 being flipped to 0 is to the left of the 0 -> 1 then the num decrease
    the opposite for an increase
    we want to flip the right most 0 that has 1s on the right of it
    once we flip that 0 to 1 we have too many 1s
    after the 0 we flip there will be a number of 1s and 0s
    clear all the bits after the 0 we flipped
        but record the count of 1s, c1
    we need to decrease the c1 by 1
    we push in c1 - 1 1s to the end of the bit representation
    """
    # compute count of 0s and count of 1s after the right most 0 with trailing 1s
    c = num
    c0 = 0
    c1 = 0
    while (c & 1) == 0 and (c != 0):
        c0 += 1
        c >>= 1
    
    while (c & 1) == 1:
        c1 += 1
        c >>= 1
    
    # error when there is no bigger number with the same number of 1s
    if c0 + c1 == 31 or c0 + c1 == 0:
        return -1

    # p is the position of the right most non-trailing zero
    p = c0 + c1

    # flip the right most non-trailing zeros
    num |= (1 << p)
    # clear all bits to the right of p
    num &= ~((1 << p) - 1)
    # insert c1 - 1 # of 1s on the right
    num |= (1 << (c1 -1)) - 1
    return num

def getPrev(num):
    # get c1 and c0
    temp = num
    c0 = 0
    c1 = 0

    while temp & 1 == 1:
        c1 += 1
        temp >>= 1
    
    if temp == 0: return 0

    while temp & 1 == 0 and temp != 0:
        c0 += 1
        temp >>= 1

    # p is the position of the right most non-trailing 1
    p = c0 + c1

    # clear bits from p to the end
    num &= ~0 << (p + 1)
    # make a mask of c1 + 1 # of 1s
    mask = 1 << (c1 + 1)
    # insert c1 + 1 1s and shift c0 - 1 bits left
    num |= mask << (c0 - 1)

    return num

# 5.5 debugger
# explain what the following code does ((n&(n-1))==0)
"""
call n = a and n - 1 = b, then a & b == 0 means that a and b have no 1 bits in the same place
if you subtract 1 from a number, in bit representation you find the 1 bit with the smallest significance
and flip it to a 0 and all the 0s after that are flipped to 1
so if n & n - 1 == 0
    then n must have no 1s before the least significant 1 -> mean it only has 1 1 bit
if a number only has 1 1 bit then the number N IS A POWER OF 2
"""

# 5.6 conversion
# write a function that will determine the number of bits you need to flip to convert A to B
def conversion(a, b):
    """
    n = a ^ b
    count the number of 1 bits in n
    """
    count = 0
    n = a ^ b

    # then count the number of 0s
    # 2 ways to do this
    # option 1
    while (n != 0):
        # increment count if n ends in a 1
        count += n & 1
        # right shift (remember python only has arithmetic shift)
        n >>= 1
    
    # option 2
    # this works because subtracting 1 toggles the right most 1 and its trailing 0s
    # then when you AND n and n - 1 your result will be n just with the right most 1 flipped to a 0
    # the rest of n will stay the same
    # good visual on pg 286
    while (n != 0):
        n = n & (n - 1)
        option2Count += 1
    return count

# 5.7 pairwise swap
# write a program to swap odd and even bits in an integer will as few instructions as possible
# basically swap bit 0 and 1. swap bit 2 and 3. swap bit 4 and 5...etc...
def pairwiseSwap(n):
    pass


