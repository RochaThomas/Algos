# morning algos
# neetcode Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights):
        # run dfs for every pacific and dfs for every atlantic
        # run through all points in grid and see if they are in both
        # retrun points in both
        pac, atl = set(), set()
        ROWS, COLS = len(heights), len(heights[0])

        def dfs(r, c, ocean, prev):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in ocean or heights[r][c] < prev:
                return
            ocean.add((r, c))
            dfs(r + 1, c, ocean, heights[r][c])
            dfs(r - 1, c, ocean, heights[r][c])
            dfs(r, c + 1, ocean, heights[r][c])
            dfs(r, c - 1, ocean, heights[r][c])

        for r in range(ROWS):
            dfs(r, 0, pac, 0)
            dfs(r, COLS - 1, atl, 0)

        for c in range(COLS):
            dfs(0, c, pac, 0)
            dfs(ROWS - 1, c, atl, 0)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res

    print(pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]))