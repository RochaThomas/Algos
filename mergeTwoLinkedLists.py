# morning algos
# neetcode merge two linked lists

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        if not list1: return list2
        elif not list2: return list1

        curr = dummy = ListNode()
        A, B = list1, list2
        if A.val > B.val:
            A, B = B, A

        while A and B:
            if A.val < B.val:
                curr.next = A
                A = A.next
            else:
                curr.next = B
                B = B.next
            curr = curr.next

        finish = A if A else B

        while finish:
            curr.next = finish
            finish = finish.next
            curr = curr.next
        
        return dummy.next

    print(mergeTwoLists([1,2,4], [1,3,4]))