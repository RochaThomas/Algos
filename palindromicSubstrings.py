# morning algos
# neetcode Palindromic Substrings

class Solution:
    def countSubstrings(self, s):
        subs = 0
        for i in range(len(s)):
            subs += self.countPali(s, i, i) + self.countPali(s, i, i + 1)
        return subs
    def countPali(self, s, l, r):
        res = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res


    print(countSubstrings("abc"))