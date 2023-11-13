# morning algos 
# neetcode meeting rooms II

class Solution:
    def min_meeting_rooms(self, intervals) -> int:
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0
        s, e = 0, 0
        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count += 1
            res = max(res, count)
        return res