
# morning algos
# neetcode Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums):
        output = [1] * len(nums)
        x = 1

        for i in range(len(nums)):
            output[i] = x
            x *= nums[i]
        x = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= x
            x *= nums[i]

        return output
