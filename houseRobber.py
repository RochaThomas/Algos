# morning algos
# neetcode House Robber

class Solution:
    def rob(self, nums):
        one, two = 0, 0
        for n in nums:
            temp = two
            two = max(one + n, two)
            one = temp
        return two

    print(rob([1,2,3,1]))