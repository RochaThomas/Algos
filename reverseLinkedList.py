# morning algos
# neetcode reverse linked list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(head):
        prev = None
        runner = head

        while runner:
            temp = runner.next
            runner.next = prev
            prev = runner
            runner = temp

            if runner == None:
                head = prev
        return head

# # recursive solution
# class Solution:
#     def reverseList(self, head):
#         if not head:
#             return None
        
#         newHead = head
#         if head.next:
#             newHead = self.reverseList(head.next)
#             head.next.next = head
#         head.next = None
#         return newHead