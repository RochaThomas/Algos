# morning algos
# neetcode find min in rotated sorted array

class Solution:
    def findMin(self, nums):
        if len(nums) == 1: return nums[0]
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m - 1] > nums[m]: return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        print("failed")

        # this solution works too but its slower and technically not O(log n)
        prev = nums[0]
        for i in range(len(nums)):
            if nums[i] < prev:
                return nums[i]
            prev = nums[i]
        return nums[0]

    print(findMin([3,4,5,1,2]))