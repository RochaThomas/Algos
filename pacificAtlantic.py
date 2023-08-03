# morning algos
# neetcode Pacific Atlantic Water Flow

class Solution:
    def pacificAtlantic(self, heights):
        res = []
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def search(r, c, visited, prevHeight):
            if ((r, c) in visited or 
                r < 0 or c < 0 or r >= ROWS or c >= COLS
                or heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            search(r + 1, c, visited, heights[r][c])
            search(r - 1, c, visited, heights[r][c])
            search(r, c + 1, visited, heights[r][c])
            search(r, c - 1, visited, heights[r][c])

        for c in range(COLS):
            search(0, c, pac, heights[0][c])
            search(ROWS - 1, c, atl, heights[ROWS - 1][c])

        for r in range(ROWS):
            search(r, 0, pac, heights[r][0])
            search(r, COLS - 1, atl, heights[r][COLS - 1])

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl: res.append([r, c])
        
        return res

    print(pacificAtlantic([
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]))