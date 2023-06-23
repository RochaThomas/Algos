# morning algos
# neetcode Last Stone Weight

import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            s1, s2 = heapq.heappop(stones), heapq.heappop(stones)
            if s1 != s2: heapq.heappush(stones, s1 - s2)

        return -stones[0] if stones else 0

    print(lastStoneWeight([2,7,4,1,8,1]))