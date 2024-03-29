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

# 3.3 stack of plates
# implement a data structure the holds a set of stacks, when a stack gets too tall, start a new one
# follow up: implement a method popAt() that props from a stack at a certain index
#   trick is do you shift to the popped stack so its full or do you operate with a stack at lower cap
"""
data stucture is an array of arrays. outer array holds multiple inner arrays
inner[0] holds a stack and inner[1] is the length of inner[0]
when inner[1] hits a specfic length start a new array with new stack with new length and append to stack_of_plates
"""

# 3.4 queue via stacks
# implement a my_queue class that implements a queue using two stacks
"""
pop all from one stack to the other then pop from the second stack to the queue

another solution is to use the second stack as the oldest and the first stack as newest
when oldest is empty, pop all from newest to oldest
when pushing just push to oldest
"""

# 3.5 sort stack
# sort a stack such that the stack is in order where the smallest is on top but the only other data structure
# you can use is another stack
"""
have a temp stack where bottom is the smallest val
temp = curr.pop()
if last.data > temp.data
then pop from max_stack to min_stack
push from temp to max
when min is empty pop all from max and push all to min
"""

# 3.6 animal shelter
# imagine there is an animal shelter that implements first in first out, you cant choose which dog or cat
# you can only choose if you want a dog or cat
# implement a data structure that models this system
"""
make a data structure, animal shelter that has an array of queues
array[0] is a queue for dogs and array[1] is for cats
dequeueAny peeks at the two queues and pops the oldest of the dogs or cats
have animal class
    -> dogs class inherits from animal
    -> cats class inherits from animal
this allows all methods to return either a cat or dog
"""