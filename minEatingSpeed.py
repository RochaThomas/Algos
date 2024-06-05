# morning algos
# neetcode koko eating bananas


import math


class Solution:
    def minEatingSpeed(self, piles, h):
        l, r = 1, max(piles)
        res = r

        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
                if hours > h:
                    l = k + 1
                    break
            if hours <= h:
                res = min(res, k)
                r = k - 1
        return res



    print(minEatingSpeed([3, 6, 7, 11], 8))