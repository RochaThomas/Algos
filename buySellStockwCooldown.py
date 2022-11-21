# morning algos
# neetcode Best Time to Buy and Sell Stock with Cooldown

class Solution:
    def maxProfit(self, prices):
        # state: buying or selling?
            # if buy i + 1
            # if sell i + 2

        # key = (i, buying) val = max_profit
        dp = {}

        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            cooldown = dfs(i + 1, buying)
            if buying:
                buy = dfs(i + 1, not buying) - prices[i]
                dp[(i, buying)] = max(buy, cooldown)
            else:
                sell = dfs(i + 2, not buying) + prices[i]
                dp[(i, buying)] = max(sell, cooldown)
            return dp[(i, buying)]
        
        return dfs(0, True)

    print(maxProfit([1,2,3,0,2]))