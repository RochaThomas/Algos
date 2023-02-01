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
