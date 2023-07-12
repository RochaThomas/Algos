# morning algos
# neetcode Task Scheduler

import collections
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        count = {}
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while maxHeap or q:
            time += 1
            if maxHeap:
                c = heapq.heappop(maxHeap) + 1
                if c:
                    q.append([c, time + n])
            if q and q[0][1] <= time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time

        

    print(leastInterval(["A","A","A","B","B","B"], 2))