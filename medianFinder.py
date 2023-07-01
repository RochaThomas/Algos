# morning algos
# neetcode Find Median of Data Stream

import heapq


class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []
        heapq.heapify(self.lower)
        heapq.heapify(self.upper)


    def addNum(self, num: int) -> None:
        if self.lower and num <= abs(self.lower[0]):
            heapq.heappush(self.lower, -num)
        else:
            heapq.heappush(self.upper, num)

        while len(self.upper) - len(self.lower) < 1:
            heapq.heappush(self.upper, abs(heapq.heappop(self.lower)))
        while len(self.upper) - len(self.lower) > 2:
            heapq.heappush(self.lower, -heapq.heappop(self.upper))

        print("lower: ", self.lower)
        print("upper: ", self.upper)
        

    def findMedian(self) -> float:
        if len(self.upper) > len(self.lower):
            return heapq.heappop(self.upper)
        else:
            return (heapq.heappop(self.upper) + abs(heapq.heappop(self.lower))) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()