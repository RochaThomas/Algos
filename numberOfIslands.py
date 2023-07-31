# morning algos
# neetcode Number of Islands

class Solution:
    def numIslands(self, grid):
        numOfIslands = 0
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])

        def search(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in visited or grid[r][c] == '0':
                return False
            visited.add((r,c))
            return (
                search(r + 1, c) or
                search(r - 1, c) or
                search(r, c + 1) or
                search(r, c - 1)
            )

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in visited: continue
                elif grid[r][c] == '1': 
                    numOfIslands += 1
                    search(r, c)
        return numOfIslands

    print(numIslands([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]))