# morning algos
# neetcode Maximum Product Subarray

class Solution:
    def maxProduct(self, nums):
        currMin, currMax = 1, 1
        res = -float('inf')

        for n in nums:
            if n == 0:
                currMin = currMax = 1
                continue
            temp = currMax * n
            currMax = max(currMax * n, currMin * n, n)
            currMin = min(temp, currMin * n, n)
            res = max(res, currMax)
        return res


    print(maxProduct([2,3,-2,4]))