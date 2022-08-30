# morning algos
# neetcode subtree of another tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        
        # in reality this next line's edge case is really evaluating if not root and subroot
        # but the first if statement already checked to make sure that subRoot is non null
        if not root:
            return False
        if self.isSameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t or s.val != t.val:
            return False
        # comment
        
        return (self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right))

    print(isSubtree([3,4,5,1,2], [4,1,2]))