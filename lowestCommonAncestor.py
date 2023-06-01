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
        # my solution directly below works and is recursive but its probably more efficient to just use a while loop
        # if (root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val): return root
        # if p.val < root.val and q.val < root.val: return self.lowestCommonAncestor(root.left, p, q)
        # if p.val > root.val and q.val > root.val: return self.lowestCommonAncestor(root.right, p, q)

        curr = root
        while curr:
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
            else:
                return curr


    print(lowestCommonAncestor(root = [6,2,8,0,4,7,9,None,None,3,5], p = 2, q = 8))