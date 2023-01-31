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
    pass


print(isPermutation("abc", "bca")) 
