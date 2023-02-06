# morning algos
# neetcode three Sum

class Solution:
    def threeSum(self, nums):
        """
        brute force O(n^3)
        3 for loops to iterate through each combination of nums, pushing to res array

        optimizing solution
        use two pointers for left and right
        sort
        if left + right > 0, then there is no number between left and right that will make it 0, so continue
        """
        res = []
        nums.sort()

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                threeSum = val + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

    print(threeSum([-1,0,1,2,-1,-4]))