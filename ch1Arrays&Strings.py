# cracking the coding interview
# chapter 1 arrays and strings

# interview questions

# 1.1 is unique
# determine if a string has all unique characters
# follow up can you do this without using additional data structures
def isUnique(str):
    letters = set()
    for c in str:
        if c in letters:
            return False
        else:
            letters.add(c)
    return True

# terrible time complexity but would work without additional data structures
# def isUnique(str):
#     for i in range(len(str) - 1):
#         for j in range(i + 1, len(str)):
#             if str[i] == str[j]:
#                 return False
#     return True
# a little better than terrible time complexity but would work without additional data structures
# def isUnique(str):
#     str.sort()
#     for i in range(len(str) - 1):
#         if str[i] == str[i + 1]:
#             return False
#     return True

# 1.2 check permutations
# write a method to check if one string is a permutation of another
def isPermutation(str1, str2):
    if len(str1) != len(str2): return False

    total1, total2 = 0, 0
    for i in range(len(str1)):
        total1 += ord(str1[i])
        total2 += ord(str2[i])

    if total1 != total2:
        return False
    return True

    # another solution is to sort the strings and compare

# 1.3 URLify
# replace spaces in the string with %20
def URLify(str):
    # cheating return str.replace(" ", "%20")
    # res = ""
    # for i in range(len(str)):
    #     if str[i] == " ":
    #         res += "%20"
    #     else:
    #         res += str[i]
    # return res

    # inplace solution
    numOfSpace = str.count(" ")
    lenOfLoop = numOfSpace * 2 + len(str)
    for i in range(lenOfLoop):
        if str[i] == " ":
            str = str[:i] + "%20" + str[i + 1:]
            i += 2
    return str

# 1.4 palindrome permutations
# write a function to check if a string has a palidromic permutation

def palindromePermutations(str):
    letters = {}
    numOdds = 0
    str = str.lower()
    for c in str:
        if c == " ":
            continue
        else:
            letters[c] = 1 + letters.get(c, 0)
            if letters[c] % 2 == 0:
                numOdds -= 1
            else:
                numOdds += 1
    
    return True if numOdds <= 1 else False

# 1.5 One Away
# given two strings, write a function that checks if they are one edit (replace, delete, insert) away from each other at most
def oneAway(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False

    longStr = str1 + str2
    letters = set()

    for i in range(len(longStr)):
        if longStr[i] in letters:
            letters.remove(longStr[i])
        else:
            letters.add(longStr[i])
    
    return True if len(letters) <= 2 else False

# 1.6 String Compression
# implement a method to perform basic string compression for repeated characters, if the compressed string wouldn't be smaller than
# the original string, return the original
def stringCompression(str):
# the solutions to this are silly, another way to do it is to count to see if the compressed string would be smaller first
# then make the compressed string after if necessary
# this makes for a horrible time complexity
    res = str[0]
    prev = str[0]
    count = 0

    for i in range(len(str)):
        if str[i] != prev:
            res += prev + count
            count = 0
        else: 
            count += 1

        prev = str[i]
    
    return res if len(res) < len(str) else str

# 1.7 Rotate Matrix
# PRACTICE THIS ONE AGAIN, HARD TO VISUALIZE
# given an n x n matrix where each pixel of the image is represented by a number can you rotate the image 90 degrees
# follow up: can you do it in place
def rotate(array):
    l, r = 0, len(array) - 1

    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            topLeft = array[top][l + i]

            array[top][l + i] = array[bottom - i][l]

            array[bottom - i][l] = array[bottom][r - i]

            array[bottom][r - i] = array[top + i][r]

            array[top + i][r] = topLeft

        r -= 1
        l += 1

    return array

# 1.8 Zero Matrix
# when an element in a matrix is 0, set the entire row and column to 0
# tricky to understand the zeroFirstRow and the last two if statements. Go over them again
def zeroMatrix(matrix):
    ROWS, COLS = len(matrix), len(matrix[0])
    zeroFirstRow = False

    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                if r > 0:
                    matrix[r][0] = 0
                else:
                    zeroFirstRow = True
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[0][c] == 0:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for c in COLS:
            matrix[0][c] = 0
    if zeroFirstRow:
        for r in ROWS:
            matrix[r][0] = 0
    return matrix

# 1.9 String Rotation
# assuming you have a method that checks if one string is a substring of another called isSubstring, write a method
# that checks if one string is a rotation of another string using only 1 call to isSubstring
def stringRotation(str1, str2):
    if len(str1) - len(str2) != 0:
        return False

    str1str1 = str1 + str1
    return str2 in str1str1
    

print(stringRotation("cathat", "hatcat"))
