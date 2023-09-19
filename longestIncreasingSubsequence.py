# morning algos
# neetcode longest increasing subsequence

class Solution:
    def lengthOfLIS(self, nums):
        if not nums: return 0
        res = 1
        subLens = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    subLens[i] = max(subLens[i], 1 + subLens[j])
                    res = max(res, subLens[i])
        return res