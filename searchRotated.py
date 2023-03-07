# morning algos
# neetcode search in rotated sorted array

class Solution:
    def search(self, nums, target):

        """
        binary search problem with a twist
        if your left is greater than your right then you are in the non sorted part of the array
            meaning the beginning of the rotation is somewhere between l and r
            if m > l then from middle to left is sorted and from middle to right is not
            if m < l then from middle to right is sorted and from middle to left is not
        if your left is less than right then you are in the sorted part of the array and you can
            just do binary search like normal
        """

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            elif nums[l] == target:
                return l
            elif nums[r] == target:
                return r
            elif nums[l] < nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1 
                else:
                    l = m + 1
        return -1
        

    print(search([4,5,6,7,0,1,2], 0))