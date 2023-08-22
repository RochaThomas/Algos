# morning algos 
# neetcode Number of Connected Components in an Undirected Graph

class Solution:
    def countComponents(self, n, edges):
        par = [i for i in range(1, n + 1)]
        rank = [1] * (n + 1)

        def find(n):
            p = par[n]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]

            return p

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return 1
        
        connected = n

        for n1, n2 in edges:
            connected -= union(n1, n2)

        return connected
        


