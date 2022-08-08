# morning algos
# neetcode add two numbers

from calendar import c


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(l1, l2):
        # pseudo
        # iterate through the length of list1
        # adding the value of list1 to list2 and instantiating that value to an output list node
        # if the value is over 10 have a store variable that will add 1 for the next node
        # if the store variable is triggered subtract 10 from the current addition
        # after the length of list1 has run
        # if list 2 still has some nodes then transfer the rest of those to the output list
        # remember to keep track of the store variable

        # figure out how to handle the case if list2 is shorter... probably use an if statement
        #  -> a while loop to run through the rest of list2 to the output list
        # make sure it works correctly for if they are both the same length
        # ...lets get to coding

        # my solution works but is a little robust
        # I will put the neetcode solution below
        # it is essentially the same method but more consicely written...so better basically 

        r1, r2, store = l1, l2, 0

        dummy = ListNode()
        output = dummy

        while r1:
            val = store + r1.val

            if store > 0:
                store = 0
            
            if val >= 10:
                val -= 10
                store = 1
            
            if not r2:
                output.next = ListNode(val)
            else:
                val += r2.val
                if val >= 10:
                    val -= 10
                    store = 1
                output.next = ListNode(val)
                r2 = r2.next
            
            r1 = r1.next
            output = output.next
        
        while r2:
            val = store + r2.val

            if store > 0:
                store = 0
            
            if val >= 10:
                val -= 10
                store += 1
            
            output.next = ListNode(val)
            r2 = r2.next  
            output = output.next     

        if store > 0:
            output.next = ListNode(1)

        return dummy.next

        # neetcode solution
        # dummy = ListNode()
        # curr = dummy

        # carry = 0
        # while l1 or l2 or carry:
        #     v1 = l1.val if l1 else 0
        #     v2 = l2.val if l2 else 0

        #     val = v1 + v2 + carry
            
        #     carry = val // 10
        #     val = val % 10

        #     curr.next = ListNode(val)

        #     curr = curr.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        # return dummy.next

    print(addTwoNumbers([2,4,3], [5,6,4]))