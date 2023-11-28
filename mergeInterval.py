# morning algos
# neetcode Merge Intervals

class Solution:
    def merge(self, intervals):
        res = []
        curr = intervals[0]

        for s, e in intervals:
            if curr[1] < s:
                res.append(curr)
                curr = [s, e]
            elif curr[1] >= s:
                curr = max(curr[1], e)
        res.append(curr)
        return res


    print(merge([[1,3],[2,6],[8,10],[15,18]]))