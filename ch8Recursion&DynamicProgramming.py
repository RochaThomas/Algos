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

# 8.2 robot in a grid
# image a robot in a grid that can only move right and now
# given a grid with certain points that are off limits, design an algo that will find if a path from the top left to the bottom right
# exists

def robot_in_a_grid(maze):
    if maze == None or len(maze) == 0: return None

    def getPath(maze, r, c, path, failed = {}):
        # if out of bounds or off limits (meaning maze[r][c] is false) or failed spot (meaning we tried and there is no path) return false
        if r < 0 or c < 0 or not maze[r][c] or (r, c) in failed:
            return False
        # if there is a path from the start to the current position then add position to path
        if (r == 0 and c == 0) or robot_in_a_grid(maze, r, c - 1, path, failed) or robot_in_a_grid(maze, r - 1, c, path, failed):
            path.add((r, c))
            return True
        # if there is no path then the position must fail so add position to failed and return False
        failed.add((r, c))
        return False
        
    path = []
    failed = {}
    # if there is a path return the path if not return None
    if (getPath(maze, len(maze) - 1, len(maze[0] - 1), path, failed)):
        return path

    return None
    