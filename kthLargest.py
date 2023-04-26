# morning algos
# neetcode Kth Largest Element in an Array

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        for i in range(len(nums)):
            nums[i] *= -1
        heapq.heapify(nums)
        while k > 0:
            res = heapq.heappop(nums)
            k -= 1
        return -res
        
    print(findKthLargest([3,2,1,5,6,4], 2))