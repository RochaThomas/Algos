# morning algos
# neetcode Swim in Rising Water

import heapq

class Solution:
    def swimInWater(self, grid):
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        direction = [[0,1], [1,0], [-1,0], [0,-1]]

        visit.add((0,0))

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N-1 and c == N - 1:
                return t
            for dr, dc in direction:
                neiR, neiC = r + dr, c + dc
                if (neiR < 0 or neiC < 0 or neiR == N or neiC == N or (neiR, neiC) in visit):
                    continue
                visit.add((neiR, neiC))
                heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])

    print(swimInWater([[0,2],[1,3]]))