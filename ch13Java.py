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

