
# morning algos
# neetcode permutation in string, check inclusion

# failed to complete
# neetcode solution was not very helpful
# i think if i try again i can come up with a working more understandable solution to this algo

# tried again this solution also failed
# def checkInclusion(s1, s2):
#     # first turn s1 into a dictionary
#     # take length of s1

#     # run a for loop where r is being kept track of
#     # if the letter is in the dictionary subtrack count by 1
#     # if the letter isnt in the letter dictionary or the letter makes the count less than 0
#     #   run a while loop to add the stuff back
#     # if the difference in pointers is the same as the length of k check if all the values are 0
#     #   if they are return true
#     # if the whole thing runs through return false

#     # maybe use a flag?

#     letter_dict = {}
#     s1_len = len(s1)
#     for letter in s1:
#         letter_dict[letter] = 1 + letter_dict.get(letter, 0)

#     incorrect = False
#     l = 0
#     for r in range(len(s2)):
#         if s2[r] in letter_dict:
#             letter_dict[s2[r]] -= 1
#             if letter_dict[s2[r]] <= 0:
#                 incorrect = True
#         else:
#             incorrect = True

#         if (r - l + 1) > s1_len:
#             incorrect = True

#         # double check if this ordering works
#         while incorrect == True:
#             if s2[l] in letter_dict:
#                 letter_dict[s2[l]] += 1
#                 incorrect = False
#             l += 1
        
#         # check all or any... i get them confused
#         if (r - l + 1) == s1_len and not any(letter_dict.values()):
#             return True
    
#     return False


# third try using 2 hashmaps and have and need
def checkInclusion(s1, s2):
    s1_letters = {}
    for letter in s1:
        s1_letters[letter] = 1 + s1_letters.get(letter, 0)

    print("s1_letters", s1_letters)

    s2_window_letters = {}
    l = 0
    have, need = 0, len(s1_letters)
    print("need", need)

    for r in range(len(s2)):
        s2_window_letters[s2[r]] = 1 + s2_window_letters.get(s2[r], 0)

        print()
        print("s2_window_letters", s2_window_letters)

        if s2[r] in s1_letters and s2_window_letters[s2[r]] == s1_letters[s2[r]]:
            have += 1
            print("added", s2[r])
        
        print("have", have)
        print("sub", s2[l:r + 1])
        
        if have == need:
            return True

        if (r - l + 1) == len(s1):
            s2_window_letters[s2[l]] -= 1
            # hacky solution here
            # because you decrement above but you are still checking what it used to be you have to add 1 in the equality check
            if s2[l] in s1_letters and s2_window_letters[s2[l]] + 1 == s1_letters[s2[l]]:
                have -= 1
                print("removed", s2[l], "have", have)
            l += 1

    return False
print(checkInclusion("trinitrophenylmethylnitramine", "dinitrophenylhydrazinetrinitrophenylmethylnitramine"))