# cracking the coding interview
# chapter 11 testing

# interview questions

# 11.1 mistake
# find the mistake in the following code
"""
unsigned int i;
for (i = 100; i >= 0; --i)
    printf("%d\n", i);

one mistake is you are using an unsigned int which is greater than or equal to 0 by definition
so it will never be less than 0 resulting in an infinite loop
second mistake is that when printing unsigned ints we need to use %u instead of %d
"""

