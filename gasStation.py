# morning algos
# neetcode Gas Station

class Solution:
    def canCompleteCircuit(self, gas, cost):
        if sum(cost) > sum(gas): return -1

        res = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total <= 0:
                total = 0
                res = i + 1
        return res
        


    print(canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))