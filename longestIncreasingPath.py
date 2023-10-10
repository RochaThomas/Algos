# morning algos
# neetcode Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(r, c, prev):
            if r >= ROWS or c >= COLS or r < 0 or c < 0 or matrix[r][c] <= prev:
                return 0
            if (r, c) in dp:
                return dp[(r, c)]
            res = 1 + max(
                dfs(r + 1, c, matrix[r][c]),
                dfs(r - 1, c, matrix[r][c]),
                dfs(r + 1, c + 1, matrix[r][c]),
                dfs(r + 1, c - 1, matrix[r][c])
            )
            dp[(r, c)] = res
            return res
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, -1)
        return max(dp.values())

    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))