# morning algos
# neetcode balanced binary tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root):
        
        def dfs(node):
            if not node:
                return [True, 0]
            left = dfs(node.left)
            if not left[0]: 
                return [False, left[1]]
            right = dfs(node.right)
            if not right[0]: 
                return [False, right[1]]
            diff = abs(left[1] - right[1])
            if diff > 1:
                return [False, diff]
            return [True, 1 + max(left[1], right[1])]
        return dfs(root)[0]


    print(isBalanced([3,9,20,None,None,15,7]))