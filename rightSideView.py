# morning algos
# neetcode binary tree right side view

# Definition for a binary tree node.
import collections


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root):
        if not root: return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            qLen = len(q)
            right = None
            for i in range(qLen):
                node = q.popleft()
                right = node
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            if right: res.append(right.val)
        return res


    print(rightSideView([1,2,3,None,5,None,4]))