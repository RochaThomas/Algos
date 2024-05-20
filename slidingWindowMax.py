
# morning algos
# neetcode sliding window maximum

import heapq
import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        res = []
        q = collections.deque()
        l = r = 0

        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            if l > q[0]:
                q.popleft()

            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res



        # -------- working solution but slow -----------
        # heap = []
        # heapq.heapify(heap)

        # res = []

        # l = 0
        # for r in range(len(nums)):
        #     heapq.heappush(heap, (-nums[r], r))
        #     if r >= k:
        #         while heap[0][1] < l:
        #             heapq.heappop(heap)
        #         res.append(-heap[0][0])
        #         l += 1
        # return res

    print(maxSlidingWindow([1,-1], 1))