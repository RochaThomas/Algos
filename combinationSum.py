# morning algos
# neetcode combination sum

class Solution:
    def combinationSum(self, candidates, target):
        res = []
        curr = []
        def backtrack(i, total):
            if total == target:
                res.append(curr[:])
            if total >= target or i >= len(candidates):
                return
            curr.append(candidates[i])
            backtrack(i, total + candidates[i])
            curr.pop()
            backtrack(i + 1, total)
        backtrack(0, 0)
        return res

    print(combinationSum([2,3,6,7], 7))