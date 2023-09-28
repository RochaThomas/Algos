# morning algos
# neetcode Word Break

class Solution:
    def wordBreak(self, s, wordDict):

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for word in wordDict:
                if dp[i]:
                    break
                if i + len(word) - 1 < len(s) and s[i : i + len(word)] == word:
                    dp[i] = dp[i + len(word)]
        return dp[0]


    print(wordBreak( "leetcode", ["leet","code"]))