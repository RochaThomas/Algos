# morning algos
# neetcode Decode Ways

class Solution:
    def numDecodings(self, s):
        if s[0] == '0': return 0
        dp = {len(s): 1}

        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                dp[i] = 0
                continue
            else:
                dp[i] = dp[i + 1]
            
            if ( i + 1 < len(s) and (s[i] == '1' or (s[i] == '2' and s[i + 1] in '0123456'))):
                dp[i] += dp[i + 2]
        return dp[0]

    print(numDecodings("12"))