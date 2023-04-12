# cracking the coding interview
# chapter 15 threads and locks

# interview questions
"""
MY UNDERSTANDING OF THREADS AND LOCKS IS NOT GOOD ENOUGH YET
MANY OF THESE SOLUTIONS JUST REFERENCE THE BOOKS SOLUTION PAGE
FIRST STUDY THIS TOPIC THEN REVISIT THESE QUESTIONS
"""

# 15.1 threads vs process
# whats the difference between a thread and a process
"""
A process is an instance of a program in execution. A process is an independent entity to which memory and CPU time are allocated
Each processes are executed seperately meaning the variables of one process cannot be accessed by another

A thread exists within a process and shares process resources. Multiple threads can exist in a process and will share process heap
space. Each thread has its own stack and registers but still can share memory through the process heap
Modifying a process resource from one thread makes the change visible to sibling threads
"""

# 15.2 context switch
# how would you measure the time spent in a context switch
"""
A context switch is the time spent switching between two processes
Record the timestamps of the last and first instruction of the processes being swapped
explanation goes over my head
watch a video and research more to understand
"""

# 15.3 dining philosophers
# A bunch of philosophers are sitting around a circular table with 1 chopstick between them. All need 2 chopsticks to eat
# and they always pick up left then right. Using threads and locks, implement a simulation of the dining philosophers problem that 
# prevents deadlocks
"""
one solution is to put down the left chopstick if there is no right chopstick to pick up
however, if the philosophers are all perfectly synchronize then all philosophers pick up left then all drop left over and over again

the better solution is to label the chopsticks with numbers and instruct the philosophers to pick up the lower number stick
meaning that they always pick up left then right except for the last philosopher who will do the reverse. This means the
philosopher could not hold a larger numbered stick unless having the lower first

solution is a little unclear without a visualization
"""

# 15.4 deadlock-free class
# design a class which provides a lock only if there are no possible deadlocks
"""
one way to prevent deadlocks is to declare what locks a process will require upfront
deadlocks happen when there is a cycle
again this solution is going over my head
get a better understanding of threads and locks and revisit these questions
solution pg 452
"""

# 15.5 call in order
# suppose we have the following code:
# public class Foo {
#   public Foo() {}
#   public void first() {}
#   public void second() {}
#   public void third() {}
# }
# The same instance of Foo will be passed to three different threads. ThreadA will call first, ThreadB will call second,
# ThreadC will call third. Design a mechanism to ensure that first is called before second and second before third
"""
solution page 456
"""

# 15.6 synchronized methods
# you are given a class with synchronized method A and a normal method B. If you have two threads in once instance of a program
# can they both execute A at the same time? Can they execute A and B at the same time?
"""
A synchronized method cannot be executed by two threads of the same instance at the same time.
If the two threads have the same instance of the object then they cannot both execute A at the same time
if they have different instances then they can be executed at the same time
A and B can be executed at the same time on differnt threads because B is not synchronized so the synchronized A method will not
lock B as long as B does not have the sync designation
"""

# 15.7 fizzbuzz
# print numbers 1 to n. When the number is divisible by 3 print Fizz, when divisible by 5 print Buzz, and when divisible by both
# print FizzBuzz. Implement a multithreaded version of FizzBuzz with 4 threads.
# One thread checks for divisibility of 3 and prints Fizz
# Another thread checks for divisibility of 5 and prints Buzz.
# Another thread checks for divisibility of 3 and 5 and prints FizzBuzz.
# The last thread prints the numbers
"""
solution pg 458
"""