# morning algos
# neetcode Reconstruct Itinerary

import collections


class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        ticketMap = {src:[] for src, dest in tickets}
        for src, dest in tickets:
            ticketMap[src].append(dest)

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in ticketMap:
                return False
            temp = list(ticketMap[src])
            for i, v in enumerate(temp):
                ticketMap[src].pop(i)
                res.append(v)
                if dfs(v):
                    return True
                ticketMap[src].insert(i, v)
                res.pop()
            return False
        
        dfs('JFK')
        return res

    print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))