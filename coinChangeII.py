# morning algos
# neetcode Coin Change II

class Solution:
    def change(self, amount, coins):
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for i in range(len(coins) - 1, -1, -1):
            nextDP = dp
            for a in range(1, amount + 1):
                if a - coins[i] >= 0:
                    nextDP[a] += nextDP[a - coins[i]]
            dp = nextDP
        return dp[amount]


    print(change(5, [1,2,5]))