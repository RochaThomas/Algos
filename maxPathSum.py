# morning algos
# neetcode binary tree maximum path sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root):
        res = [root.val]

        def dfs(root):
            if not root: return 0
            leftMax = dfs(root.left)
            rightMax = dfs(root.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            res[0] = max(root.val + leftMax + rightMax, res[0])
            return root.val + max(leftMax, rightMax)

        dfs(root)
        return res[0]

    print(maxPathSum([1,2,3]))