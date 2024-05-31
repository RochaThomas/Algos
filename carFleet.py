# morning algos
# neetcode car fleet

class Solution:
    def carFleet(self, target, position, speed):
        pairs = [[p, s] for p, s in zip(position, speed)]
        res = []

        for p, s in sorted(pairs)[::-1]:
            t = (target - p) / s
            if not res or res[-1] < t:
                res.append(t)
            
        return len(res)

    print(carFleet(10, [6,8], [3,2]))