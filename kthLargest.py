# morning algos
# neetcode Kth Largest Element in an Array

import heapq

# testing

class Solution:
    def findKthLargest(self, nums, k):

        nums = [-n for n in nums]

        # above is just a short hand for the code below
        # for i in range(len(nums)):
        #     nums[i] = -nums[i]

        minHeap = heapq.heapify(nums)

        res = 0
        for i in range(k):
            res = heapq.heappop(nums)
        
        return -res
        
    print(findKthLargest([3,2,1,5,6,4], 2))