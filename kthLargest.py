# morning algos
# neetcode Kth Largest Element in an Array

import heapq


class Solution:
    def findKthLargest(self, nums, k):
        
        heapq.heapify(nums)

        while len(nums) >= k:
            curr = heapq.heappop(nums)
        return curr
        
    print(findKthLargest([3,2,1,5,6,4], 2))