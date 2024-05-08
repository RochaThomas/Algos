

# morning algos
# neetcode longest repeating character replacement

class Solution:
    def characterReplacement(self, s, k):
        count = {}
        res = 0
        l = 0
        maxF = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            maxF = max(maxF, count[s[r]])
            while (r - l + 1) - maxF > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res


    print(characterReplacement("AABABBA", 1))