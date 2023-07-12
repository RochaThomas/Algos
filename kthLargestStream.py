# morning algos
# neetcode kth largest element in a stream

import heapq


class KthLargest:

    def __init__(self, k, nums):
        self.k = k
        self.nums = nums
        heapq.heapify(self.nums)

    def add(self, val):
        if len(self.nums) < self.k or val > self.nums[0]: heapq.heappush(self.nums, val)
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
