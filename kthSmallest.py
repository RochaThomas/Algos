# morning algos
# neetcode Kth Smallest Element in a BST

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root, k):
        # n is the number of nodes that we have visited
        n = 0
        stack = []
        curr = root

        while curr and stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            n += 1
            if n == k:
                return curr.val
            curr = curr.right


    print(kthSmallest([3,1,4,None,2], 1))