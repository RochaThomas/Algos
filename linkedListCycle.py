# morning algos
# neetcode linked list cycle

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head):
        """
        two solutions
        first is make a hashmap checking to see if the current node is already in the map
        second is to use a runner moving twice as fast
        """
        curr = runner = head
        while runner and runner.next:
            curr = curr.next
            runner = runner.next.next
            if curr == runner:
                return True
        return False


    print(hasCycle([3,2,0,-4]))