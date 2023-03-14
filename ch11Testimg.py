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

# 11.2 random crashes
# An application crashes when it runs. You are given the source. After running it 10x in a debugger, it never crashes in the same place
# The app is single threated and uses only the c standard library. What programming errors could be causing this crash?
# How would you test each one?
"""
There are many different answers to this one
It mainly depends on the application. Think about problems within the app and problems arising outside the app
4 main things in the app could be happening: random variable, uninitialized variable, memory leak, and external dependencies
learn as much about the app as possible then maybe search for one of these mistakes
if nothing fixes it then try to see if any other external applications running in the system are interfering with the crashing app
"""

