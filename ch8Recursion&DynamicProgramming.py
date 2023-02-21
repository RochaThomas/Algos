# cracking the coding interview
# ch 8 recursion and dynamic programming

# interview questions

# 8.1 triple step
# a child is running up a stair case with n steps and can take either 1, 2, or 3 steps at a time
# implement a method to count how many possible ways the child can run up the steps

def triple_step(n, memo = {}):
    """
    paths from a step to the end are step + 1, step + 2, or step + 3
    """
    if n < 0 : return 0
    elif n == 0: return 1
    elif n in memo: return memo[n]
    else: 
        memo[n] = triple_step(n - 1, memo) + triple_step(n - 2, memo) + triple_step(n - 3, memo)

    return memo[n]


print(triple_step(4))

# 8.2 robot in a grid
# image a robot in a grid that can only move right and now
# given a grid with certain points that are off limits, design an algo that will find a path from the top left to the bottom right

def robot_in_a_grid(off_limits):
    pass