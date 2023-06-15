# morning algos
# neetcode binary tree maximum path sum

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(node):
            if not node: return 0
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            res[0] = max(res[0], left + right + node.val)
            return node.val + max(left, right)

        dfs(root)
        return res[0]
        

    print(maxPathSum([1,2,3]))