# morning algos
# neetcode min stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]

# this solution works!!! but its kind of slow and bad with memory
# class Node:
#     def __init__(self, val):
#         self.value = val
#         self.min = val

# class MinStack:
#     """
#     initialize stack initializes array with no values
#     push appends value to array
#     pop removes last value from array
#     top returns last value from array
#     getMin is difficult for O(1) time
#         couple different ways to implement
#             getMin iterates through stack every time its called and returns the min
#             stack has a min variable that holds the min
#                 push has the potential to update min depending on value
#                 pop checks to see if the pop value is the min, if it is  iterate through stack for new min
#             last and probably the best way is to use nodes
#                 the stack should be a list of nodes where every node has a min variable
#                 when it is pushed to the stack then the min at the time of that push is recorded for that node
#                 so to get the min you just look at the min var of the top of the stack
#                 when a value is popped the min will still be at the top of the stack even if the prev min was popped
#     """

#     def __init__(self):
#         self.stack = []

#     def push(self, val: int) -> None:
#         node = Node(val)
#         if  self.stack[-1] and node.value > self.stack[-1].min:
#             node.min = self.stack[-1].min
#         self.stack.append(node)

#     def pop(self) -> None:
#         self.stack.pop()

#     def top(self) -> int:
#         return self.stack[-1].value

#     def getMin(self) -> int:
#         return self.stack[-1].min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()