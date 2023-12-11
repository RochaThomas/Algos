# morning algos 
# neetcode Detect Squares

import collections


class DetectSquares:

    def __init__(self):
        self.ptsCount = collections.defaultdict(int)
        self.pts = []

    def add(self, point):
        self.ptsCount[tuple(point)] += 1
        self.pts.append(point)

    def count(self, point):
        res = 0
        px, py = point
        for x, y in self.pts:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            res += self.ptsCount[(x, py)] * self.ptsCount[(px, y)]
        return res