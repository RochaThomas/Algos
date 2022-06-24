

# morning algos
# neetcode longest repeating character replacement

# didn't work because edge case where first char is the least frequent
# def characterReplacement(s, k):
#     l, r = 0, 1
#     longest = 0
#     replacement_count = 0
#     curr_length = 1

#     while l < len(s) and len(s) - l > longest:
#         if s[l] == s[r]:
#             curr_length += 1
#         elif replacement_count < k:
#             curr_length += 1
#             replacement_count += 1
#         else:
#             longest = max(longest, curr_length)
#             curr_length = 1
#             l += 1
#             r = l

#         if r + 1 > len(s) - 1:
#             longest = max(longest, curr_length)
#             curr_length = 1
#             l += 1
#             r = l
#         r += 1

#     return longest

# solution
def characterReplacement(s, k):
    count = {}
    longest = 0

    l = 0
    maxf = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)
        maxf = max(maxf, count[s[r]])

        while (r - l + 1) - maxf > k:
            count[s[l]] -= 1
            l += 1
        longest = max(longest, r - l + 1)
    return longest

print(characterReplacement("AABABBA", 1))