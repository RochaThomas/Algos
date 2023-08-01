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

        def helper(node):
            if node:
                if node.val in nodeMap:
                    return
                nodeMap[node.val] = [neighbor.val for neighbor in node.neighbors]
                for neighbor in node.neighbors:
                    helper(neighbor)

        helper(node)
        
        newNodes = {}
        for key in nodeMap.keys():
            newNodes[key] = Node(key)
        for key in newNodes.keys():
            for neighborIndex in nodeMap[key]:
                newNodes[key].neighbors.append(newNodes[neighborIndex])
            # print(key, ', ', [neigh.val for neigh in newNodes[key].neighbors])
        return newNodes.get(1)

        


    print(cloneGraph([[2,4],[1,3],[2,4],[1,3]]))