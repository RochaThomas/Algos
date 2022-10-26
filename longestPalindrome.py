# morning algos
# neetcode Longest Palindromic Substring

class Solution:
    def longestPalindrome(self, s):
        res = ""
        resLen = 0

        for i in range(len(s)):
            # check odd length first
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                newLen = r - l + 1
                if newLen > resLen:
                    resLen = newLen
                    res = s[l:r+1]
                r += 1
                l -= 1

            # check even length
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]: 
                newLen = r - l + 1
                if newLen > resLen:
                    resLen = newLen
                    res = s[l:r+1]
                r += 1
                l -= 1
        return res
    print(longestPalindrome("babad"))