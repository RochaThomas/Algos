
# morning algos
# neetcode minimum window substring

# solution is viable but unsurprisingly takes too long

# def minWindow(s, t):
#     if len(t) == 1:
#         if t in s:
#             return t
#     elif t == s:
#         return t
#     elif len(t) > len(s):
#         return ""
    
#     shortest_length = len(s) + 1
#     shortest_sub = ""
#     letter_dict = {}

#     for letter in t:
#         if letter in letter_dict:
#             letter_dict[letter] += 1
#         else: 
#             letter_dict[letter] = 1

#     print(letter_dict)

#     for l in range(len(s)-len(t) + 1):
#         if s[l] in letter_dict:
#             substring_dict = {}
#             substring_dict[s[l]] = 1
#             r = l + 1
#             print(substring_dict)
#             while substring_dict != letter_dict:
#                 if s[r] in letter_dict:
#                     if s[r] in substring_dict:
#                         if substring_dict[s[r]] < letter_dict[s[r]]:
#                             substring_dict[s[r]] += 1
#                     else:
#                         substring_dict[s[r]] = 1

#                 if substring_dict == letter_dict:
#                     sub_len = r - l + 1
#                     if sub_len < shortest_length:
#                         shortest_length = sub_len
#                         shortest_sub = s[l:r + 1]

#                 if r == len(s) - 1:
#                     break

#                 r += 1
#     return shortest_sub

# second try at a more efficient solution
# neetcode solution
def minWindow(s,t):
    if t == "": return ""
    
    letter_dict, window = {},{}

    for letter in t:
        letter_dict[letter] = 1 + letter_dict.get(letter, 0)
    
    have, need  = 0, len(letter_dict)

    shortest_sub, shortest = "", len(s) + 1
    l = 0

    for r in range(len(s)):
        letter = s[r]
        window[letter] = 1 + window.get(letter, 0)

        if letter in letter_dict and window[letter] == letter_dict[letter]:
            have += 1

        while have == need:
            if (r - l + 1) < shortest:
                shortest_sub = s[l : r + 1]
                shortest = r - l + 1

            window[s[l]] -= 1
            if s[l] in letter_dict and window[s[l]] < letter_dict[s[l]]:
                have -= 1
            l += 1
    return shortest_sub if shortest != len(s) + 1 else ""


print(minWindow("ADOBECODEBANC", "ABC"))