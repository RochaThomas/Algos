# morning algos
# neetcode count good nodes in binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root):
        
        def dfs(node, pMax):
            if not node: return 0
            res = 0
            if node.val >= pMax:
                res += 1
            pMax = max(node.val, pMax)
            res += dfs(node.left, pMax)
            res += dfs(node.right, pMax)
            return res
        return dfs

    print(goodNodes([3,1,4,3,None,1,5]))