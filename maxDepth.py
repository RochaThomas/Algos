# morning algos
# neetcode maximum depth of binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root):
        if not root: return 0
        def helper(node, currDepth):
            if not node:
                return currDepth
            return max(helper(node.left, currDepth + 1), helper(node.right, currDepth + 1))
        return max(helper(root.left, 1), helper(root.right, 1))
    
    print(maxDepth([3,9,20,None,None,15,7]))