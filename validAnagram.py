# morning algos
# neetcode Valid Anagram

class Solution:
    def isAnagram(self, s, t):
        if len(s) != len(t): return False
        sCount = {}
        tCount = {}
        for i in range(len(s)):
            sCount[s[i]] = sCount.get(s[i], 0) + 1
            tCount[t[i]] = tCount.get(t[i], 0) + 1

        for key in sCount.keys():
            if sCount[key] != tCount.get(key, 0):
                return False
        return True

        # simple solution
        return sorted(s) == sorted(t)

    print(isAnagram("anagram", "nagaram"))