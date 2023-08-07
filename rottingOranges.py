# morning algos
# neetcode Rotting Oranges

class Solution:
    def orangesRotting(self, grid):
        rotten = []
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    rotten.append([r,c])

        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        while fresh > 0 and rotten:
            for i in range(len(rotten)):
                r, c = rotten.pop(0)
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] != 1:
                        continue
                    grid[row][col] = 2
                    rotten.append([row, col])
                    fresh -= 1
            time += 1
        
        return time if fresh == 0 else -1



    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))