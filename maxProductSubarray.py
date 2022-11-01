# morning algos
# neetcode Maximum Product Subarray

class Solution:
    def maxProduct(self, nums):
        res = max(nums)
        currMin, currMax = 1, 1

        for n in nums:
            if n == 0:
                currMin, currMax = 1, 1
                continue
            temp = currMax * n
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(temp, n * currMin, n)
            res = max(res, currMax)
        return res


    print(maxProduct([2,3,-2,4]))