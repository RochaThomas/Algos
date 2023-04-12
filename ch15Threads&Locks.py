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