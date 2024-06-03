# morning algos
# neet code binary search

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return -1

    print(search([5], 5))