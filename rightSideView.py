# morning algos
# neetcode binary tree right side view

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


import collections


class Solution:
    def rightSideView(self, root):
        output = []

        if not root:
            return output

        q = collections.deque()
        q.append(root)
        
        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                node = q.popleft()

                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)

            if level:
                output.append(level[-1])
        
        return output


    print(rightSideView([1,2,3,None,5,None,4]))