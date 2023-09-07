# morning algos
# neetcode House Robber

class Solution:
    def rob(self, nums):
        start0, start1 = 0, 0
        for n in nums:
            temp = max(n + start0, start1)
            start0 = start1
            start1 = temp
        
        return start1

    print(rob([1,2,3,1]))