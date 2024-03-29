# cracking the coding interview
# chapter 12 c and c++

# interview questions
# this will only be a rough overview of the questions and solutions for this chapter

# 12.1 last k lines
# write a method to print the last K lines of an input file using C++
"""
usually you would have to do 1 read to get the total number of lines
then another read to print out the last k lines
however if you use a circular array you can do both in one read
an array allows you to save k lines in the array
making it circular allows you to keep track of the oldest entry and keep you from shifting
every time you insert a new line in the array
basically you have an array with another var that keeps track of the index of the oldest entry
if the var reaches the length k, then reset it to 0
when there are no more lines to insert
var will tell you the oldest line and the array will contain the k last lines
"""

# 12.2 reverse string
# implement a function void reverse(char* str) in C or C++ which reverses a null terminated string
"""
void reverse(char* str) {
    char temp;
    if (str) {
        while (*end) { 
            # find the end of the string by iterating through the string
            ++end
        }
        # set end back 1 so its the last letter since end would be at null
        --end
        # swap chars at the beginning of the string with chars at the end of the string
        # until the pointers meet
        while (str < end) {
            temp = *str;
            *str++ = *end;
            *end-- = tmp;
        }
    }
}
"""

# 12.3 hash table vs stl map
# compare and contrast a hash table and an stl map. how is a hash table implemented? if the number of 
# inputs is small, which data structure can be used instead of a hash table
"""
a hash table hashes a key that finds the index where the value is stored. It uses chaining for storing
multiple values at a particular index to avoid collisions
An STL map inserts key value pairs in a binary search tree and does not have to deal with handling
collisions
The search time for a hash table is O(1) while an STL's is O(log n)

A hash table is implemented by using an array of linked lists where each node in the linked list stores
the value and the original key
    we use a good hash function to distribute the keys well (decreases collisions)
    need a method to handle collisions which are inevitable (usually through chaining but there are
        other ways)
    need methods to dynamically increase or decrease the size of the hash table

An STL map or a binary search tree can be used instead of a hash table if there is a small number of
values to be stored because the difference in performance between the O(log n) stl map and the O(1)
search time of the hash map would be negligable
"""

# 12.4 virtual functions
# how do virtual functions work in C++
"""
Virtual functions depend on vtables. Vtables are constructed when a class function is declared as virtual.
This table stores the addresses of the virtual functions of this class.
If a derived class does not override the virtual function then the derived class's vtable stores the
reference to the parent class's vtable
"""

# 12.5 shallow vs deep copy
# what is the difference between a deep and a shallow copy? explain how you would use each.
"""
A shallow copy copies all the member values from one object to another. A deep copy does all this
and also deep copues any pointer objects

Shallow copies are generally used when passing information about a complex structure without actual
duplication of data. Must be careful when deleting shallow copies. Shallow copies are rarely used.
"""

# 12.6 volatile
# what is the significance of the keyword volatile in C?
"""
Volatile tells the compiler that the value of variable it is applied to can change from the outside
without any update done by the code. This can be caused by the hardware, OS, or another thread.
Because it can change, the complier will reload the value each time from memory
Volatile can be used well in multithreaded programs
"""

# 12.7 virtual base class
# why does a deconstructor in a base class need to be declared virtual?
"""
virtual functions are used to call the most derived implementation of a function.
call the child version of a function not the parent
so deconstructors must be virtual so that it can erase the object of type child from memory
it is of type child not parent so it won't work if its not virtual
"""

# 12.8 copy node
# write a method that takes a pointer to a node structure as a parameter and returns a complete copy of the passed
# in data structure. the node data structure contains two pointers to other nodes 
"""
maintain a hash map from a node address in the original structure to the corresponding node in the new copy
this allows us to recreate the structure while also detecting loops
"""

# 12.9 smart pointer
# write a smart pointer class. smart pointer is a data type that simulates a pointer and provides automatic garbage colletion
# it automatically counts the number of references to a smart pointer object and frees the object of type T when the reference
# count hits 0
"""
COMPLICATED PROBLEM TO THINK THROUGH WITHOUT HINTS AND HELP
needs a reference count var that increments when we add a new reference to the obj
needs constructor and deconstructor
    constructor points to obj and sets counter to 1
    deconstructor decrements every time a reference is destroyed
        frees the memory if the decrement results in ref count to be 0
need to handle when one smart pointer points to another
    decrement old and increment new when this happens
"""

# 12.10 malloc
# write an aligned malloc and free function that supports allocatiing memory such that the memory address returned
# is divisible by a specific power of two
"""
DO FURTHER RESEARCH TO UNDERSTAND THE QUESTION FIRST AND THEN THE SOLUTION
"""

# 12.11 2d alloc
# write a function in c called my2DAlloc which allocates a 2d array. Minimize the number of calls to malloc and make sure that
# the memory is accessible by the notation arr[i][j]
"""
DO FURTHER RESEARCH TO UNDERSTAND THE QUESTION FIRST AND THEN THE SOLUTION
create a 1d array of pointers
for each array index, create a new 1d array
this gives a 2d array that can be accessed through array indices

to decrease malloc calls
the array that each pointer is pointing to is stored in contiguous memory
first the pointer array than each individual array follows one after another

this continguous memory solution also allows us to free the memory in 1 call
"""