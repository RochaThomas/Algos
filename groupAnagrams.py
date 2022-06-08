

# morning algos
# group anagrams neetcode 150 #4

# create a dictionary of letters for the first word
# push it to an array
# remove the word from the original array
# check all the other words to see if they are anagrams of the first
# if they are push it to the same array as the checking word and remove it from the original array
# once the length of the array has been reached start over with the new first word
# when there are no more words...return the output

# works but leetcode time limit exceeded

# def groupAnagrams(strs):
#     output = []

#     x = 0

#     while x < len(strs):
#         letter_dict = {}
#         group = []
        
#         for letter in strs[x]:
#             if letter in letter_dict:
#                 letter_dict[letter] += 1
#             else:
#                 letter_dict[letter] = 1
        
#         group.append(strs[x])
#         strs.remove(strs[x])

#         i = 0

#         while i < len(strs):
#             isAnagram = True
#             temp_dict = letter_dict.copy()
#             for letter in strs[i]:
#                 if letter in temp_dict:
#                     temp_dict[letter] -= 1
#                 else:
#                     isAnagram = False
#                     break

#             if any(temp_dict.values()):
#                 isAnagram = False
            
#             if isAnagram == True:
#                 group.append(strs[i])
#                 strs.remove(strs[i])
#             else:
#                 i += 1
        
#         output.append(group)


#     return output

# more optimal solution
def groupAnagrams(strs):
    output = []
    sorted_letter_dict = {}

    for word in strs:
        sortedWord = "".join(sorted(word))
        if sortedWord not in sorted_letter_dict:
            sorted_letter_dict[sortedWord] = [word]
        else:
            sorted_letter_dict[sortedWord].append(word)
    
    for val in sorted_letter_dict.values():
        output.append(val)
    
    return output

print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))