# cracking the coding interview
# chapter 13 java

# interview questions

# 13.1 private constructor
# in terms of inheritance what is the purpose of keeping a constructor private?
"""
making a constructor private means you can only access the constructor if you can also access it's private methods
the only things that can access these private methods are the class itself, the inner classes of this class, and the other
inner classes of this classes parent class
meaning if A and B are inner classes of Q and C is an inner class of A then ABC can access the private constructor

This demonstrate inheritance because a subclass calls its parent's constructor. Meaning the A class can be inherited by its own
subclasses or by its parent's other subclasses
"""

# 13.2 return from finally
# in java does the finally block get executed if we insert a return statement inside the try block of a try-catch-finally?
"""
yes
the finally block gets executed when the try block exits regardless of return, continue, break, etc
the finally block only doesn't execute if the virtual machine exits before the finally block begins executing
or if the thread that is running the try catch block gets killed
"""

# 13.3 final, etc
# what is the difference between final, finally, and finalize?
"""
genrally
final - controls whether a method, variable, or class is changeable
finally - is used in a try/catch block to make sure a piece of code always runs
finalize - is a method called by the garbage collector once it determines no more references exist

specifics
final
    when applied to primitive var, value can not change
    when applied to var reference, the reference cannot change to point to another obj on the heap
    when applied to a method, the method cannot be overridden
    when applied to a class, the class cannot be subclassed
finally
    this block executes even if an exeption is thrown
    its usually used to clean up code
finalize
    this is called just before the automatic garbage collector actually destroys an obj
    this method can be overridden if someone wishes to define custom behavior for garbage collection
"""

