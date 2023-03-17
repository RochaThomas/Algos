# morning algos
# neetcode add two numbers

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        A, B = l1, l2
        dummy = res = ListNode()
        carry = 0

        while A and B:
            digit = A.val + B.val + carry
            res.next = ListNode(digit % 10)
            res = res.next
            carry = digit // 10
            A = A.next
            B = B.next

        if not A and not B and carry == 0:
            return dummy.next
        elif not A and not B and carry > 0:
            res.next = ListNode(carry)
            return dummy.next
        else:
            cont = A if A else B
            if carry == 0:
                res.next = cont
            else:
                while cont:
                    digit = cont.val + carry
                    res.next = ListNode(digit % 10)
                    res = res.next
                    carry = digit // 10
                    cont = cont.next
                if carry > 0:
                    res.next = ListNode(carry)
        return dummy.next


    print(addTwoNumbers([2,4,3], [5,6,4]))