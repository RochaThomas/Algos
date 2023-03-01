# morning algos
# neet code binary search

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            midpoint = l + ((r - l) // 2)
            if nums[midpoint] == target:
                return midpoint
            elif nums[midpoint] < target:
                l = midpoint + 1
            else:
                r = midpoint - 1
        
        return -1

    print(search([5], 5))