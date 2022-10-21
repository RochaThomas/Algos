# morning algos
# neetcode Min Cost Climbing Stairs

class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append(0)

        for i in range(len(cost) - 3 ,  -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
        
        return min(cost[0], cost[1])


    print(minCostClimbingStairs([10,15,20]))