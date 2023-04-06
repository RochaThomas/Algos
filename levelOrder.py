# morning algos
# neetcode binary tree level order traversal

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root):
        q = collections.deque()
        q.append(root)
        res = []

        while q:
            qLen = len(q)
            level = []
            for i in range(qLen):
                curr = q.popleft()
                if curr:
                    q.append(curr.left)
                    q.append(curr.right)
                    level.append(curr.val)
            if level:
                res.append(level)
        
        return res




    print(levelOrder([3,9,20,None,None,15,7]))
    