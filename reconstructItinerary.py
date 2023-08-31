# morning algos
# neetcode Reconstruct Itinerary

class Solution:
    def findItinerary(self, tickets):
        tickets.sort()
        adj = {src:[] for src, dest in tickets}
        for src, dest in tickets:
            adj[src].append(dest)

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                res.append(v)
                adj[src].pop(i)
                if dfs(v): return True

                adj[src].insert(i, v)
                res.pop()
            return False
        dfs('JFK')
        return res
            


    print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))