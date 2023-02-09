# morning algos
# neetcode best time to buy and sell stock aka max profit

class Solution:
    def maxProfit(self, prices):
        """
        iterate through
        record min, if runner < min, min = runner and shift index to runner and increment runner
        record maxProfit, for every iteration of runner see if runner - min > then max profit
        """
        minPrice, maxProfit = float("inf"), 0
        for i in range(len(prices)):
            profit = prices[i] - minPrice
            if profit < 0:
                minPrice = prices[i]
            elif profit > 0:
                maxProfit = max(profit, maxProfit)

        return maxProfit if maxProfit > 0 else 0

        # another way to write this solution making it more obvious that it is a sliding window problem is using l and r pointers
        # l , r = 0, 1
        # maxProfit = 0

        # while r < len(prices):
        #     if prices[l] < prices[r]:
        #         profit = prices[r] - prices[l]
        #         maxProfit = max(maxProfit, profit)
        #     else:
        #         l = r
        #     r += 1
        # return maxProfit


    print(maxProfit([7,1,5,3,6,4]))