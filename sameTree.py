# morning algos
# neetcode same tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p, q):
        if not p and not q: return True
        elif not p or not q or p.val != q.val: return False
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        
    print(isSameTree([1,2,3], [1,2,3]))