# morning algos
# neetcode Swim in Rising Water

import heapq


class Solution:
    def swimInWater(self, grid):
        ROWS, COLS = len(grid), len(grid[0])
        minHeap = [[grid[0][0], 0, 0]]
        visit = set()

        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1],
        ]
        
        while minHeap:
            t, a, b = heapq.heappop(minHeap)
            if a == ROWS - 1 and b == COLS - 1:
                return t
            for dr, dc in directions:
                r, c = dr + a, dc + b
                if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in visit:
                    continue
                visit.add((r, c))
                heapq.heappush(minHeap, [max(t, grid[r][c]), r, c])


    print(swimInWater([[0,2],[1,3]]))