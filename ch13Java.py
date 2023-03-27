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

