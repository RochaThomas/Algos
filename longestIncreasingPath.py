# morning algos
# neetcode Longest Increasing Path in a Matrix

class Solution:
    def longestIncreasingPath(self, matrix):
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = {}

        def dfs(i, j, prev):
            if i < 0 or j < 0 or i >= ROWS or j >= COLS or matrix[i][j] <= prev:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 1 + max(dfs(i + 1, j, matrix[i][j]), dfs(i - 1, j, matrix[i][j]), dfs(i, j + 1, matrix[i][j]), dfs(i, j - 1, matrix[i][j]))
            return dp[(i, j)]
        
        for i in range(ROWS):
            for j in range(COLS):
                dfs(i, j, matrix[i][j] - 1)
        return max(dp.values())

    print(longestIncreasingPath([[9,9,4],[6,6,8],[2,1,1]]))