# morning algos
# neetcode Subsets II

class Solution:
    def subsetsWithDup(self, nums):
        res = []
        curr = []
        nums.sort()

        def backtrack(i):
            if i >= len(nums):
                res.append(curr[:])
                return
            curr.append(nums[i])
            backtrack(i + 1)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1

            curr.pop()
            backtrack(i + 1)
        backtrack(0)
        return res

    print(subsetsWithDup([1,2,2]))