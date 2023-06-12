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
        # max(maxLeft + maxRight + )
        res = [root.val]
        def dfs(node):
            if not node: return 0
            left = dfs(node.left)
            left = max(left, 0)
            right = dfs(node.right)
            right = max(right, 0)
            res[0] = max(res[0], node.val + left + right)
            return node.val + max(left, right)
        return max(dfs(root), res[0])
        

    print(maxPathSum([1,2,3]))