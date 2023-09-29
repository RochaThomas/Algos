# morning algos
# neetcode Unique Paths

class Solution:
    def uniquePaths(self, m, n):
        dp = [[0] * n] * m
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = 1
                else:
                    dp[r][c] = dp[r - 1][c] + dp[r][c -1]
        return dp[m - 1][n - 1]

    print(uniquePaths(3, 7))