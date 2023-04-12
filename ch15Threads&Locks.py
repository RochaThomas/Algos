# cracking the coding interview
# chapter 15 threads and locks

# interview questions

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