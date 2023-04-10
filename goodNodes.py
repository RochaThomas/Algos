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
        """
        keep track of min in current path
        if less than min than node is good
        """
        def dfs(node, pathMax):
            if not node:
                return 0
            res = 1 if node.val >= pathMax else 0
            pathMax = max(pathMax, node.val)
            res += dfs(node.left, pathMax) + dfs(node.right, pathMax)
            return res

        return dfs(root, root.val)
            

    print(goodNodes([3,1,4,3,None,1,5]))