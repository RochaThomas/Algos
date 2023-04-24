# morning algos
# neetcode Last Stone Weight

import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if second > first:
                heapq.heappush(stones, first - second)
        
        return abs(stones[0]) if stones else 0

    print(lastStoneWeight([2,7,4,1,8,1]))