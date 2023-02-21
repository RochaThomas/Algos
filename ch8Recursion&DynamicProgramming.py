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
    
# 8.3 magic index
# a magic index in an array if defined to be an index such that A[i] = i. given a sorted array of distinct integers
# write an algo to find a magic index if one exists in array A

# def magic_index(a, offset = 0):
    """
    if the value at the beginning of the array is already larger than a certain index, then the magic index cannot be between
    the beginning of the array and the index of the value at the beginning of the array
        thus you skip to the index of the beginning value and try again
    
    if a[i] > i: skip to a[a[i]]
    if a[i] < i: keep interating through the array
    if a[i] == i return i
    else return False
    """
    # i believe this code would work but... the book has a different solution
    # for i in range(len(a)):
    #     val = a[i]
    #     if val > i + offset:
    #         return magic_index(a[val: ], offset + i)
    #     elif val == i + offset:
    #         return val
    
    # return False

# initial is (a, 0, len(a) - 1)
def magic_fast(a, start, end):
    """
    similar to binary search, given sorted and distinct values
    a little tough to understand so look at book example array closely to understand why we know where to look
    """
    if end < start:
        return -1
    mid = (start + end) / 2
    if a[mid] == mid:
        return mid
    # if the value at mid is too large then the magic index must be to the left
    elif a[mid] > mid:
        magic_fast(a, start, mid - 1)
    # if the value at mid is too small then the magic index must be to the right becasue we have distinct nums
    # so because mid is already that value then array[value] cannot also be the value at mid
    else:
        return magic_fast(a, mid + 1, end)

def magic_fast_non_distinct(a, start, end):
    if end < start:
        return -1
    mid = (start + end) / 2
    if a[mid] == mid:
        return mid
    
    # search left
    # take the min here because with non distinct values
    # the magic index could still appear
    # imagine mid = 5 and a[5] = 2 but a[2] = 2 as well
    leftIndex = min(mid - 1, a[mid])
    left = magic_fast_non_distinct(a, start, leftIndex)
    if left >= 0:
        return left
    
    # search right
    rightIndex = max(mid + 1, a[mid])
    right = magic_fast_non_distinct(a, rightIndex, end)
    
    return right

# 8.4 power set
# write a method to return all subsets of a set
def power_set(s):
    pass