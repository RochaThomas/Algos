# cracking the coding interview
# chapter 2 linked lists

# interview questions

class Node(object):
    def __init__(self, data = None, n = None):
        self.data = data
        self.next = n

class LinkedList(object):
    def __init__(self, head):
        self.head = head

    def append(self, data):
        new_node = Node(data)
        curr = self.head
        while curr.next != None:
            curr = curr.next
        curr.next = new_node
        return True
    
    def length(self):
        curr = self.head
        total = 0
        while curr.next != None:
            total += 1
            curr = curr.next
        return total

    def display(self):
        elem = []
        curr = self.head
        while curr.next != None:
            elem.append(curr.data)
            curr = curr.next
        print(elem)
        return elem
    
    def remove(self, data):
        curr = self.head
        prev = None
        
        if curr.data == data:
            self.head = curr.next
            return True

        while (curr):
            if curr.data == data:
                prev.next = curr.next
                return True
            else:
                prev = curr
            curr = curr.next
        return False

# 2.1 Remove Dup
# write code to remove duplicates from an unsorted linked list
# follow up: how can you do this without a buffer (hashtable, array, set, etc)?

    def remove_dup(self):
        elements = set()

        curr = self.head
        prev = None
        while curr != None:
            if curr.data not in elements:
                elements.add(curr.data)
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next
        return

    """
    the above code runs in O(n) time with O(n) space
    however this can be done without a buffer, it would just be slower
    similar to a nested for loop
    use one pointer (curr) to go through the linked list
    use another pointer (runner) to go through the entire list checking to see if the data matches the data of curr
    if it does remove it (change the next pointers) and keep going
    once the runner hits the end of the linked list, curr = curr.next and runner resets to the new curr's .next
    this runs in O(1) space but O(n^2) time
    """

# 2.2 Return Kth to Last
# implement an algorithm that returns the Kth to last element of a singlely linked list

    def kth_to_last(self, k):
        curr_idx = 0
        runner_idx = 0

        curr = self.head
        runner = curr

        while runner_idx - curr_idx != k:
            runner = runner.next

        while runner.next != None:
            runner = runner.next
            curr = curr.next

        return curr.data

# 2.3 Delete Middle Node
# delete a node from a linked list (not the head or end) without having access to the head, you only have access to
# the specific node
    def delete_middle_node(self, node):
        if node.next == None or node == None:
            return False
        node.data = node.next.data
        node.next = node.next.next
        return True

# 2.4 Partition
# write code that partitions a linked list by a certain value. All nodes less than the partition value are first then all values
# greater than the partition follow. The partition value does not have to separate the two halves

    def partition(self, x):
        # iterate through linkedlist
        # add smaller vals to one list and larger to another list
        # then link the two at the end

        curr = self.head
        new_head = Node()
        start = new_head.next
        partition_point = Node()
        back_half = partition_point.next

        while curr != None:
            if curr.data < x:
                start.next = curr
                start = start.next
            else:
                back_half.next = curr
                back_half = back_half.next
            curr = curr.next
        
        start.next = partition_point.next
        
        return new_head.next

# 2.5 Sum Lists
# given two linkedlist where each node represents a digit of a number, find the sum. The linked lists are stored in
# reverse order
# follow up: repeat this question if the link lists were reversed
# find video for follow up question

    def sum_lists(self, list1, list2):
        l1 = list1.head
        l2 = list2.head

        res_head = Node()
        res = res_head.next()

        while l1 != None and l2 != None:
            new_digit = Node(data = l1.data + l2.data + carry)
            res.next = new_digit
            res = res.next

            carry = new_digit.data // 10
            
            l1 = l1.next
            l2 = l2.next

        if carry > 0:
            res.next = Node(data = carry)

        # if one is longer than the other
        if l1 != None:
            while l1 != None:
                l1.data = l1.data + carry
                carry = l1.data // 10
                res.next = l1
                res = res.next
                l1 = l1.next
        elif l2 != None:
            while l2 != None:
                l2.data = l2.data + carry
                carry = l2.data // 10
                res.next = l2
                res = res.next
                l2 = l2.next
        
        return res_head.next

# 2.6 Palindrome
# implement a function to check if the linked list a palindrome
# watch video on recursive solution
    def palindrome(self):
        curr = self.head
        runner = curr
        stack = []

        while runner != None and runner.next != None:
            stack.append(curr.data)
            runner = runner.next.next
            curr = curr.next

        # accounting for an odd number of nodes
        if runner != None:
            curr = curr.next

        while curr != None:
            top = stack.pop()
            if curr.data != top:
                return False
            curr = curr.next

        return True

# 2.7 Intersection
# given two singlely linked lists determine if the two lists intersect by reference

    def intersection(self, list1, list2):
        l1, l1_len, l1_none = list1.head, 0, False
        l2, l2_len, l2_none = list2.head, 0, False

        # first get lengths and see which is longer
        while l1 != None and l2 != None:
            l1_len += 1
            l2_len += 1
            
            l1 = l1.next
            l2 = l2.next
            if l1 == None:
                l1_none = True
            if l2 == None:
                l2_none = True
        
        # get tails
        if l1_none:
            while l1:
                l1_len += 1
                l1 = l1.next
        if l2_none:
            while l2:
                l2_len += 1
                l2 = l2.next

        # if tails aren't equal then return False
        if l1 != l2:
            return False

        # reset runners
        l1 = list1.head
        l2 = list2.head
        
        # make list the same length
        if l1_len > l2_len:
            for i in range(l1_len - l2_len):
                l1 = l1.next
        elif l2_len > l1_len:
            for i in range(l2_len - l1_len):
                l2 = l2.next

        # compare nodes by reference and return intersection
        while l1 != None and l2 != None:
            if l1 == l2:
                return l1

        return False

# 2.8 Loop Detection
# determine if a linked list contains a loop and return the node at the beginning of the loop if one exists
# watch a video on this solution, hard to visualize
    def loop_detection(self):
        curr = self.head
        runner = self.head

        while curr != None and runner != None:
            curr = curr.next
            runner = runner.next.next
            if curr == runner:
                break

        # no collision no loop
        if runner == None or runner.next == None:
            return False

        curr = self.head
        while curr != runner:
            curr = curr.next
            runner = runner.next

