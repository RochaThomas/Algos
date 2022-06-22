
# morning algos
# neet code longest substring without repeating characters

# this solution works... but lets see if we can make it faster
# def lengthOfLongestSubstring(s):
#     if not s: return 0

#     l, r = 0, 1
#     longest = 1

#     char_dict = {s[l]:1}

#     curr_length = 1

#     while r < len(s):
#         if s[r] not in char_dict:
#             char_dict[s[r]] = 1
#             r += 1
#             curr_length += 1
#         elif s[r] in char_dict:
#             longest = max(curr_length, longest)
#             l += 1
#             r = l + 1
#             char_dict = {s[l]:1}
#             curr_length = 1

#         if r + 1 > len(s):
#             longest = max(curr_length, longest)

#     return longest

# more efficient solution than above
# the nested while loop is more efficient in the case that you need to take
# multiple chars off of the front to start a new non repeating substring

def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    longest = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1
        charSet.add(s[r])
        longest = max(longest, r - l + 1)
    return longest



print(lengthOfLongestSubstring("abcabcbb"))