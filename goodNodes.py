# morning algos
# neetcode count good nodes in binary tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root):

        def checkNode(max, curr):
            if not curr:
                return 0
            elif curr.val < max:
                return (checkNode(max, curr.left) + checkNode(max, curr.right))
            
            return 1 + (checkNode(curr.val, curr.left) + checkNode(curr.val, curr.right))

        return checkNode(root.val, root)



    print(goodNodes([3,1,4,3,None,1,5]))