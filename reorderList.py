# morning algos
# neetcode reorder list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head):
        """
        get half, reverse second half of list, merge lists
        """

        slow = head
        fast = head.next

        # get to half
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None

        while second:
            temp = second.next
            second.next  = prev
            prev = second
            second = temp

        # merge
        first = head
        second = prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2



    print(reorderList([1,2,3,4]))