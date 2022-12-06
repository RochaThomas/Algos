# morning algos
# neetcode Maximum Subarray

class Solution:
    def maxSubArray(self, nums):
        maxSub = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(maxSub, curSum)
        return maxSub

    print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))