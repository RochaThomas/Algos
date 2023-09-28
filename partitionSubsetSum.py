# morning algos
# neetcode Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums):
        if sum(nums) % 2: return False

        target = sum(nums) // 2
        dp = set()
        dp.add(0)
        for n in nums:
            nextDP = set()
            for val in dp:
                if n + val == target: return True
                nextDP.add(val)
                nextDP.add(val + n)
                dp = nextDP
        return False

    print(canPartition([1,5,11,5]))