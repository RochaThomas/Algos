# morning algos
# neetcode subtree of another tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot: return True
        if not root: return False
        
        if self.checkTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    def checkTree (self, node, subRoot):
        if not node and not subRoot: return True
        if node and subRoot and node.val == subRoot.val:
            return self.checkTree(node.left, subRoot.left) and self.checkTree(node.right, subRoot.right)
        return False


    print(isSubtree([3,4,5,1,2], [4,1,2]))