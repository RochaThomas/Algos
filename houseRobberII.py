# morning algos
# neetcode House Robber II

class Solution:
    def rob(self, nums):
        return max(self.helper(nums[1:]), self.helper(nums[:-1]), nums[0])
    def helper(self, houses):
        one, two = 0, 0
        for h in houses:
            temp = two
            two = max(one + h, two)
            one = temp
        return two

    print(rob([2,3,2]))