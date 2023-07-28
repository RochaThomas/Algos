# morning algos
# neetcode combination sum II

class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []

        def backtrack(pos, curr, total):
            if total == target:
                res.append(curr[:])
            if pos >= len(candidates) or total >= target:
                return
            
            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                curr.append(candidates[i])
                backtrack(i + 1, curr, total + candidates[i])
                curr.pop()
                prev = candidates[i]

        backtrack(0, [], 0)
        return res

    print(combinationSum2([10,1,2,7,6,1,5], 8))