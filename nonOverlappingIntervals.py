# morning algos
# neetcode Non-overlapping Intervals

class Solution:
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()

        prev = intervals[0][1]
        count = 0
        for s, e in intervals:
            if s < prev:
                count += 1
                prev = min(prev, e)
            else:
                prev = e
        return count

    print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))