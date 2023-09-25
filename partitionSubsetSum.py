# morning algos
# neetcode Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums):
        total = sum(nums)
        if total % 2: return False
        target = total // 2
        if target in nums: return True

        dp = set()
        dp.add(0)

        for i in range(len(nums) - 1, -1, -1):
            nextDP = set()
            for t in dp:
                if (t + nums[i]) == target: return True
                nextDP.add(t + nums[i])
                nextDP.add(t)
            dp = nextDP
        return False

    print(canPartition([1,5,11,5]))