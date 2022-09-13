# morning algos
# neetcode Last Stone Weight

import heapq


class Solution:
    def lastStoneWeight(self, stones):
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            firstStone = heapq.heappop(stones)
            secondStone = heapq.heappop(stones)

            if firstStone != secondStone:
                newStone = firstStone - secondStone
                heapq.heappush(stones, newStone)
            
        stones.append(0)
        return abs(stones[0])
        
        

    print(lastStoneWeight([2,7,4,1,8,1]))