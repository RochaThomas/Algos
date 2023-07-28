# morning algos
# neetcode combination sum II

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(i, total, curr):
            if total == target:
                res.append(curr[:])
            if total >= target or i >= len(candidates):
                return

            prev = -1
            for j in range(i, len(candidates)):
                if prev == candidates[j]:
                    continue
                curr.append(candidates[j])
                backtrack(j + 1, total + candidates[j], curr)
                curr.pop()
                prev = candidates[j]
            
        backtrack(0, 0, [])
        return res

    print(combinationSum2([10,1,2,7,6,1,5], 8))