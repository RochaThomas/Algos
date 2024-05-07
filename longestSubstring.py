
# morning algos
# neet code longest substring without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s):
        if not s: return 0
        letters = set()
        l, r = 0, 1
        res = 1
        letters.add(s[l])

        while r < len(s):
            while s[r] in letters:
                letters.remove(s[l])
                l += 1
            letters.add(s[r])
            r += 1
            res = max(res, r - l)
        return res
        
    print(lengthOfLongestSubstring("abcabcbb"))