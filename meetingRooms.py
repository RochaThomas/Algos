# morning algos 
# neetcode meeting rooms

class Solution:
    def can_attend_meetings(self, intervals) -> bool:
        intervals.sort()
        prev = intervals[0][0] - 1
        for start, end in intervals:
            if start < prev:
                return False
            prev = end
        return True