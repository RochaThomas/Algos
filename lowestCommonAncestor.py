# morning algos
# neetcode lowest common ancestor of a binary search tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        curr = root

        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr

    print(lowestCommonAncestor(root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8))