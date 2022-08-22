# morning algos
# neetcode reverse nodes in k-group

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseKGroup(self, head, k):
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            # reverse the group
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

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1

        return curr

    print(reverseKGroup([1,2,3,4,5], 2))