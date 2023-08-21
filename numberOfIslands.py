# morning algos
# neetcode Number of Islands

class Solution:
    def numIslands(self, grid):
        res = 0
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == '0' or grid[r][c] == 'x':
                return
            grid[r][c] = 'x'
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == '1':
                    res += 1
                    dfs(r, c)
        return res

    print(numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))