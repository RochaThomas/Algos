# morning algos
# neetcode validate binary search tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root):
        
        def dfs(node, low, high):
            if not node: return True
            if node.val >= high or node.val <= low: return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, -float('inf'), float('inf'))
        

    print(isValidBST([2,1,3]))

