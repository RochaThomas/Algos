# morning algos
# neetcode Task Scheduler

import collections
import heapq


class Solution:
    def leastInterval(self, tasks, n):
        count = collections.Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0

        # pairs of [-count, idleTime]
        q = collections.deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time



    print(leastInterval(["A","A","A","B","B","B"], 2))