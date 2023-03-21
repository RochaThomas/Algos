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