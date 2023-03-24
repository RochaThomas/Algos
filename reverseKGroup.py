# morning algos
# neetcode reverse nodes in k-group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        """
        partition into smaller lls that are the size of k
        send to helper function to reverse, maybe use a temp node to hold the place of a section to be reverse
        connect end of reversed to begin of the next section
        """
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp

        return dummy.next

    def getKth(self, node, k):
        curr = node
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    print(reverseKGroup([1,2,3,4,5], 2))