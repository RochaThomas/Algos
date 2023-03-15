

# morning algos
# neetcode remove Nth node from End of list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        l, r = dummy, head

        while n > 0 and r:
            r = r.next
            n -= 1

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next

        return head


    print(removeNthFromEnd([1,2,3,4,5], 2))
        