# morning algos
# neetcode Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals):
        if len(intervals) <= 1: return 0

        intervals.sort()
        res = 0
        prevEnd = intervals[0][0]
        for start, end in intervals:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)
        return res

    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))