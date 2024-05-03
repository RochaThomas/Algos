# morning algos
# neetcode best time to buy and sell stock aka max profit

class Solution:
    def maxProfit(self, prices):
        buy = float("inf")
        res = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            else:
                res = max(res, prices[i] - buy)
        return res

    print(maxProfit([7,1,5,3,6,4]))