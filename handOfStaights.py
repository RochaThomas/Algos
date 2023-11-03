# morning algos
# neetcode Hand of Straights

import heapq


class Solution:
    def isNStraightHand(self, hand, groupSize):
        if len(hand) % groupSize: return False
        count = {}
        for n in hand:
            count[n] = count.get(n, 0) + 1

        heap = list(count.keys())
        heapq.heapify(heap)

        while heap:
            curr = heap[0]
            if count[curr] == 0:
                print("pop ", heapq.heappop(heap))
                continue
            print("curr ", curr)
            for i in range(curr, curr + groupSize):
                if i not in count or count[i] == 0: return False
                count[i] -= 1
        
        return True

    print(isNStraightHand([1,2,3,6,2,3,4,7,8], 3))