# morning algos
# neetcode combination sum II

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(curr, pos, target):
            if target == 0:
                res.append(curr.copy())
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(curr, i + 1, target - candidates[i])
                curr.pop()
                prev = candidates[i]
            
        backtrack([], 0, target)

        return res
            

    print(combinationSum2([10,1,2,7,6,1,5], 8))