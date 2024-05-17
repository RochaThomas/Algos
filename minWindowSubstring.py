
# morning algos
# neetcode minimum window substring
class Solution:
    def minWindow(self, s, t):
        if not t: return ""
        if len(t) > len(s): return ""

        sDict = {}
        tDict = {}

        for i in range(len(t)):
            tDict[t[i]] = tDict.get(t[i], 0) + 1
        
        matches = 0
        goal = len(tDict)
        
        res = [float("inf"), 0, 0]
        l = 0
        for r in range(len(s)):
            sDict[s[r]] = sDict.get(s[r], 0) + 1
            if s[r] in tDict and tDict[s[r]] == sDict[s[r]]:
                matches += 1

            while matches == goal:
                windowLen = r - l + 1
                if windowLen < res[0]:
                    res = [windowLen, l, r + 1]
                sDict[s[l]] -= 1
                if s[l] in tDict and tDict[s[l]] > sDict[s[l]]:
                    matches -= 1
                l += 1
        
        return s[res[1]: res[2]]

    print(minWindow("ADOBECODEBANC", "ABC"))