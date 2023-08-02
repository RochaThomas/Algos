# morning algos
# neetcode Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid):
        res = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        
        def search(r, c):
            if (r >= ROWS or r < 0 or c >= COLS or c < 0 or (r, c) in visited or grid[r][c] == 0):
                return 0
            else:
                visited.add((r, c))
                return (1 + search(r + 1, c) + search(r - 1, c) + search(r, c + 1) + search(r, c - 1))
            

        for r in range(ROWS):
            for c in range(COLS):
                count = search(r, c)
                if count > 0:
                    res = max(res, count)
                    count = 0
        return res

    print(maxAreaOfIsland([
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]))