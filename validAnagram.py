# morning algos
# neetcode Valid Anagram

class Solution:
    def isAnagram(self, s, t):

        # faster solution using more memory
        # time: O(n)
        # space: O(n)
        if len(s) != len(t):
            return False

        countS , countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True

        # slower solution using constant memory
        # time: O(nlog)
        # space: O(1)
        # return sorted(s) == sorted(t)
    print(isAnagram("anagram", "nagaram"))