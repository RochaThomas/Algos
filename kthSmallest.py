# morning algos
# neetcode Kth Smallest Element in a BST

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root, k):
        """
        list all of the nodes in order from least to greatest
        when the length of the list == k return the last node
        push left then curr then right
        """
        stack = []
        count = 0
        curr = root

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.val
            curr = curr.right


    print(kthSmallest([3,1,4,None,2], 1))