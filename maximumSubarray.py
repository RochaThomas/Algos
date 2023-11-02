# morning algos
# neetcode Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        res = nums[0]
        curr = 0

        for n in nums:
            if curr < 0:
                curr = 0
            curr += n
            res = max(res, curr)
        return res



    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))