# morning algos
# neetcode K Closest Points to Origin


import heapq


class Solution:
    def kClosest(self, points, k):
        minHeap = []

        for x,y in points:
            distance  = (x ** 2) + (y ** 2)
            minHeap.append([distance, x, y])

        heapq.heapify(minHeap)

        output = []
        
        for i in range(k):
            distance, x, y = heapq.heappop(minHeap)
            output.append([x, y])
        
        return output

    print(kClosest([[1,3],[-2,2]], 1))
        