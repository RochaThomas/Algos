# morning algos
# neetcode Last Stone Weight

import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            larger, large = heapq.heappop(stones), heapq.heappop(stones)
            if larger != large:
                heapq.heappush(stones, larger - large)
        return -stones[0] if stones else 0


    print(lastStoneWeight([2,7,4,1,8,1]))