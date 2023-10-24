# morning algos
# neetcode Jump Game

class Solution:
    def canJump(self, nums):
        maxIdx = 0

        for i in range(len(nums)):
            maxIdx = max(maxIdx, i + nums[i])
            if maxIdx >= len(nums) - 1: return True
            if maxIdx == i: return False
        return False

    print(canJump([2,3,1,1,4]))