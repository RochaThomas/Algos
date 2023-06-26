# morning algos
# neetcode K Closest Points to Origin

import heapq


class Solution:
    def kClosest(self, points, k):
        
        # make a heap
        # push to heap until heap length is k long
        # push tuples (distance from origin, [x, y])
        # run through all points
        # return heap points only

        h = []
        heapq.heapify[h]

        for p in points:
            # distance from origin, point
            curr = (-(p[0] ** 2 + p[1] ** 2), [p[0], p[1]])
            heapq.heappush(h, curr)
            while len(h) > k:
                heapq.heappop(h)
        
        res = [p[1] for p in h]
        return res

    print(kClosest([[1,3],[-2,2]], 1))
        