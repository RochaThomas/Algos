# morning algos
# neetcode Burst Ballons

class Solution:
    def maxCoins(self, nums):
        dp = {}
        nums = [1] + nums + [1]

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in dp: return dp[(l, r)]
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i -1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]

        return dfs(1, len(nums) - 2)

    print(maxCoins([3,1,5,8]))