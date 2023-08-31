# morning algos
# neetcode Min Cost to Connect All Points

import heapq


class Solution:
    def minCostConnectPoints(self, points):
        visit = set()
        res = 0

        minHeap = [(0, points[0][0], points[0][1])]

        while len(visit) < len(points):
            d, x, y = heapq.heappop(minHeap)
            if (x, y) in visit:
                continue
            visit.add((x, y))
            res += d
            for x2, y2 in points:
                if (x2, y2) in visit: continue
                dist =  abs(x - x2) + abs(y - y2)
                heapq.heappush(minHeap, (dist, x2, y2))
        return res


    print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))