

# slow version
# def isAnagram(word, test_word):
#     letter_dict = {}

#     for letter in word:
#         if letter in letter_dict:
#             letter_dict[letter] += 1
#         else:
#             letter_dict[letter] = 1


#     for letter in letter_dict:
#         count = 0
#         for i in range(len(test_word)):
#             if test_word[i] == letter:
#                 count += 1

#         if count != letter_dict[letter]:
#             return False
    
#     word_set = set(word)
#     test_word_set = set(test_word)

#     if len(word_set) != len(test_word_set):
#         return False

#     return True

# more optimal solution
from getopt import gnu_getopt


def isAnagram(word, test_word):
    letter_dict = {}

    for letter in word:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    
    for letter in test_word:
        if letter in letter_dict:
            letter_dict[letter] -= 1
        else:
            return False

    return not any(letter_dict.values())

print(isAnagram("anagram", "znagaram"))