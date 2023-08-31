# morning algos
# neetcode Network Delay Time

import heapq

class Solution:
    def networkDelayTime(self, times, n, k):
        visit = set()
        adj = {i:[] for i in range(1, n + 1)}
        for s, d, t in times:
            adj[s].append([d, t])

        minHeap = [[0, k]]
        t = 0

        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visit: continue
            visit.add(node)
            t = max(time, t)

            for src, w in adj[node]:
                if src not in visit:
                    heapq.heappush(minHeap, [time + w, src])

        return t if len(visit) == n else -1
            



    print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))