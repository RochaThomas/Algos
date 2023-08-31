# morning algos
# neetcode Network Delay Time

import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        time = 0
        visit = set()
        adj = {i:[] for i in range(1, n + 1)}
        minHeap = [[0, k]]
        for src, dest, t in times:
            adj[src].append([dest, t])

        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = max(t, time)
            for nei, w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [time + w, nei])

        return time if len(visit) == n else -1
            



    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))