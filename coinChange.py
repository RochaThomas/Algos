# morning algos 
# neetcode Coin Change

class Solution:
    def coinChange(self, coins, amount):
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(1 + dp[a - c], dp[a])
        return dp[amount] if dp[amount] != amount + 1 else -1


    print(coinChange([1,2,5], 11))