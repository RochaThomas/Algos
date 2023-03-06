# morning algos
# neetcode find min in rotated sorted array

class Solution:
    def findMin(self, nums):
        """
        everything to the left must be less than the right
        run binary search to find where the value to the immediate left it greater than the right
        that value is the min
        """
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if nums[m - 1] > nums[m]:
                return nums[m]
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        return -1

    print(findMin([3,4,5,1,2]))