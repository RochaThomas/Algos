# morning algos
# neetcode Rotting Oranges

import collections


class Solution:
    def orangesRotting(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        fresh, time = 0, 0
        q = collections.deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1: fresh += 1
                elif grid[r][c] == 2: q.append([r, c])

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]

        while q and fresh > 0:
            for i in range(len(q)):
                row, col = q.popleft()
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] != 1:
                        continue
                    q.append([r, c])
                    fresh -= 1
                    grid[r][c] = 2
            time += 1
        
        return time if fresh == 0 else -1
                


    print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))