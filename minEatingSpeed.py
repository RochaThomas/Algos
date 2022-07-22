# morning algos
# neetcode koko eating bananas


# pseudo
# number k is related to the number of piles and the number of hours given
# not sure...


# neetcode solution
# change it into a binary search problem
# test all the value rates from the lowest (smallest pile) to the highest (largest pile)
# instead of iterating through 1 by 1
# use a binary search to find the min viable eating rate
# run the binary until the very end

import math


def minEatingSpeed(piles, h):
    l, r  = 1, max(piles)
    result = r

    while l <= r:
        k = (l + r) // 2
        totalHours = 0
        for p in piles:
            totalHours += math.ceil(p/k)
        
        if totalHours > h:
            l = k + 1
        elif totalHours <= h:
            result = k
            r = k - 1


    return result

print(minEatingSpeed([3, 6, 7, 11], 8))