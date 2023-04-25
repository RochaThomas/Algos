# morning algos
# neetcode K Closest Points to Origin

import heapq


class Solution:
    def kClosest(self, points, k):
        
        minHeap = []
        for x,y in points:
            dist = (x**2) + (y**2)
            minHeap.append([dist,x,y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
        return res

    print(kClosest([[1,3],[-2,2]], 1))
        