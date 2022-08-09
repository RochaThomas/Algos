# morning algos
# neetcode linked list cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# works but there is actually a faster O(1) solution
class Solution:
    def hasCycle(head):
        # prevNodes = {}

        # runner = head
        # while runner:
        #     prevNodes[runner] = runner.next
        #     if runner.next in prevNodes:
        #         return True
            
        #     runner = runner.next
        
        # return False

        # neetcode solution O(1)
        s, f = head, head

        while f and f.next:
            s = s.next
            f = f.next.next
            if s == f:
                return True

        return False


    print(hasCycle([3,2,0,-4]))