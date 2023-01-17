# morning algos
# neetcode Missing Number

class Solution:
    def missingNumber(self, nums):
        res = len(nums)

        for i in range(len(nums)):
            res += (i - nums[i])
        return res

    print(missingNumber([3,0,1]))