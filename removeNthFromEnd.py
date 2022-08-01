

# morning algos
# neetcode remove Nth node from End of list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(head, n):
        dummy = ListNode(0, head)

        l, r = dummy, head
        for i in range(n):
            r = r.next

        while r:
            l = l.next
            r = r.next

        l.next = l.next.next
        
        return dummy.next


    print(removeNthFromEnd())