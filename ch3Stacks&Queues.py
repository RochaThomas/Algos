# cracking the coding interview
# chapter 3 stacks and queues

# interview questions

# 3.1 three in one
# describe how you can use a single array to implement three stacks
"""
the question is basically asking how can you fit the space needed for 3 stacks in the space of one array
https://stackoverflow.com/questions/4770627/how-to-implement-3-stacks-with-one-array
great answer above
one stack pushes to the front of the array
2nd stack pushes to the end of the array
3rd stack starts in the middle and pushes to alternating sides of the midpoint
    5 3 1 h 0 2 4 6 where h is at the midpoint
    if one side is going to collide with one of the stacks then shift the whole stack left or right depending
    on where the collision will occur
"""


# 3.2 stack min
# how would you design a stack such that it has the functions push() pop() and min() that all operate in O(1) time
"""
implement min stack node to record local min
meaning each node records the min when it is added to the stack
so when the min is popped off the min of the top of the stack is the min of the whole stack
when a node is added to the stack compare val of node to min and record local min for that node
"""


