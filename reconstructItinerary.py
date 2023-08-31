# morning algos
# neetcode Reconstruct Itinerary

class Solution:
    def findItinerary(self, tickets):
        tickets.sort()

        adj = {frm:[] for frm, to in tickets}
        for src, dst in tickets:
            adj[src].append(dst)

        res = ['JFK']

        def dfs(src):
            if len(res) == len(tickets) + 1:
                return True
            if src not in adj:
                return False
            temp = list(adj[src])
            for i, v in enumerate(temp):
                adj[src].pop(i)
                res.append(v)
                if dfs(v): return True

                adj[src].insert(i, v)
                res.pop()
            return False
        dfs('JFK')
        return res


    print(findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))