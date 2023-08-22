# morning algos
# neetcode Clone Graph


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node):
        nodeMap = {}

        def dfs(node):
            if node in nodeMap:
                return nodeMap[node]
            copy = Node(node.val)
            nodeMap[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None

    print(cloneGraph([[2,4],[1,3],[2,4],[1,3]]))