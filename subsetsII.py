# morning algos
# neetcode Subsets II

class Solution:
    def subsetsWithDup(self, nums):
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i >= len(nums):
                res.append(subset[:])
                return
            
            subset.append(nums[i])
            backtrack(i + 1, subset)

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            
            subset.pop()
            backtrack(i + 1, subset)

        backtrack(0, [])
        return res



    print(subsetsWithDup([1,2,2]))