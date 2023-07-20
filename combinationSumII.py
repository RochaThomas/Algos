# morning algos
# neetcode combination sum II

class Solution:
    def combinationSum2(self, candidates, target):
        res = []
        candidates.sort()

        def backtrack(j, total, curr):
            if total == target:
                res.append(curr[:])
                return
            if j >= len(candidates) or total > target:
                return
            
            prev = - 1
            for i in range(j, len(candidates)):
                if candidates[i] > target:
                    return
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, total + candidates[i], curr)

                curr.pop()
                prev = candidates[i]
            
        backtrack(0, 0, [])
        return res

    print(combinationSum2([10,1,2,7,6,1,5], 8))