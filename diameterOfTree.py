# morning algos
# neetcode diameter of binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root):
        res = [0]

        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            right = dfs(node.right)
            res[0] = max(res[0], left + right)
            return 1 + max(left, right)

        dfs(root)
        return res[0]

    print(diameterOfBinaryTree([1,2,3,4,5]))