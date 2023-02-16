
# morning algos
# neetcode sliding window maximum

import collections


class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        brute force
        iterate through nums, for every iteration of the window, iterate through window to find max
        time: O(n*k) where n is len of nums and k is the size of the window
        space: O(1)

        optimizing
        use an external variable that keeps track of the max
        problem is if you lose the max when the window shifts how do you find the next max fast
            two ideas
                first is you just iterate through the new window if max is no longer in the window
                    not ideal but it would minimize the iterations of size k depending on nums
                second is to use some type of heap, min or max not sure yet
                    when max is out then pop max and new max will be whatevers next up in the heap
                        problem with this is how to pop values off of max heap when they aren't the max but are
                        shifted out of the window
        """
        res = []
        l = r = 0
        q = collections.deque()
        
        while r < len(nums):
            # pop any values to left of the max if they are smaller
            while q and nums[q[-1]] < nums[r]:
                q.pop()

            # add the next value
            q.append(r)
            
            # pop off the number that is not longer in the window after shift
            if l > q[0]:
                q.popleft()

            # append the max as long as the window is the length of k
            if (r + 1) >= k:
                res.append(nums[q[0]])

            r += 1
        return res


    print(maxSlidingWindow([1,-1], 1))