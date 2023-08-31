# morning algos
# neetcode Network Delay Time

import heapq


class Solution:
    def networkDelayTime(self, times, n, k):
        adj = {i:[] for i in range(1, n + 1)}
        for src, dst, time in times:
            adj[src].append([dst, time])
        
        minHeap = [[0, k]]
        time = 0
        visit = set()

        while minHeap:
            t, node = heapq.heappop(minHeap)
            if node in visit:
                continue
            visit.add(node)
            time = max(t, time)
            for nei, w in adj[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, [t + w, nei])
        return time if len(visit) == n else -1
            



    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))