# cracking the coding interview
# ch 8 recursion and dynamic programming

"""
I AM HAVING TROUBLE WITH RECURSION
MOST OF THESE SOLUTIONS WERE JUST "TRANSLATED" FROM THE TEXTBOOK
IM DOING THIS TO GET THE FEEL FOR THE SYNTAX AND SEE THE PATTERNS OF RECURSIVE SOLUTIONS
I NEED TO STUDY THIS MORE AND PROBABLY WATCH SOME VIDEOS ON PYTHON RECURSION AND EXAMPLE PROBLEMS
WITH IN DEPTH VIDEO SOLUTIONS
"""
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

# this makes no sense to me. lets what a video
# neetcode explains a python solution susinctly
# video is neetcode Subsets - Backtracking - Leetcode 78
def power_set(s, i):
    all_subsets = []

    subset = []
    
    def get_subset(i):
        if i >= len(s):
            all_subsets.append(subset.copy())
            return
        # there are two decisions for creating subsets of every value of every index
        # to add the value or to not add the value
        # add the value
        subset.append(s[i])
        get_subset(i + 1)

        # not adding the value
        subset.pop()
        get_subset(i + 1)
    
    get_subset(0)
    return all_subsets

# 8.5 recursive multiply
# write a recursive function to multiply two positive integers without using the * or / operators
# you can use + - or bit shifting

def recursive_multiply(a, b):
    bigger = a if a > b else b
    smaller  = a if a < b else b

    def helper(smaller, bigger):
        if smaller == 0: return 0
        elif smaller == 1: return bigger

        s = smaller >> 1
        halfProd = helper(s, bigger)

        if smaller % 2 == 0:
            return halfProd + halfProd
        else:
            return halfProd + halfProd + bigger

    return helper(smaller, bigger)

# 8.6 towers of hanoi
# you have 3 towers of n disks of different sizes which can slide onto any tower
# puzzle starts with disks sorted in ascending order from top to bottom
# rule
#   only one disk can be moved at a time
#   a disk is slid off the top of one tower onto another
#   a disk cannot be placed on top of a smaller disk
# write a program to move all the disks from the first tower to the last using stacks
def towers_of_hanoi():
    """
    solution to this problem involves object oriented programming 
    check page 354 for solution
    the solution idea is
        base case: when n = 0 return
        move top n - 1disks from origin to buffer, using destination as a buffer
        move top from origin to destination
        move top n - 1 disks from buffer to destination, using origin as a buffer
    """
    pass

# 8.7 permutations without dups
# write a method to compute all permutations of a string of unique characters
def perms_without_dups(s):
    length = len(s)
    res = []
    # base case
    if length == 0:
        res.append("")
        return res
    
    for i in range(length):
        # remove char i and find permutations of remaining chars
        before =  s[:i]
        after = s[i + 1:]
        # partials will find permutations of all the chars in s minus s[i]
        partials = perms_without_dups(before + after)
        for strings in partials:
            res.append(s[i] + strings)

    return res

# 8.8 permutations with duplicates
# write a method to compute all permutations of a string whose characters are not necessarily unique. the list of permutations should
# not have duplicates

def perms_with_dups(s):
    res = []

    def build_freq_table(s):
        hash = {}
        for c in s:
            hash[c] = 1 + hash.get(c, 0)
        return hash

    def helper(table, prefix, remaining, res):
        # base case
        if remaining == 0:
            res.add(prefix)
            return

        # try remaining letters for next perm and generate remaining permutations
        for c in table.keys():
            count = table.get(c)
            if count > 0:
                table[c] -= 1
                helper(table, prefix + c, remaining - 1, res)
                table[c] = count

    table = build_freq_table(s)
    helper(table, "", len(s), res)

    return res

# 8.9 parens
# implement an algorithm to print all valid combinations of n pairs of parenthesis
def parens(n):
    def add_parens(list, left_rem, right_rem, str, index):
        # invalid state
        if left_rem < 0 or right_rem  < left_rem: return

        if left_rem == 0 and right_rem == 0:
            list.append(str.copy)
        else:
            # add right and recurse
            str[index] = '('
            add_parens(list, left_rem, right_rem - 1, str, index + 1)

    str = []
    list = []
    add_parens(list, n, n, str, 0)
    return list

# 8.10 paint fill
# create a paint fill function like one might see on image editing programs
# given a screen (represented by a 2D array of colors), a point, and a new color, fill in the surrounding
# area until the color changes from the original color

# GOOD PRACTICE QUESTION
# IMAGINE DEPTH FIRST SEARCH ON A GRAPH
def paint_fill(screen, row, col, new_color):
    if screen[row][col] == new_color: return False
    def paint_fill_helper(screen, row, col, old_color, new_color):
        if row < 0 or row >= len(screen) or col < 0 or col >= len(screen[0]):
            return False
        if screen[row][col] == old_color:
            screen[row][col] == new_color
            # up 1 pixel
            paint_fill_helper(screen, row + 1, col, old_color, new_color)
            # right 1 pixel
            paint_fill_helper(screen, row, col + 1, old_color, new_color)
            # down 1 pixel
            paint_fill_helper(screen, row - 1, col, old_color, new_color)
            # left 1 pixel
            paint_fill_helper(screen, row, col - 1, old_color, new_color)
        return True

    return paint_fill_helper(screen, row, col, screen[row][col], new_color)

# 8.11 coins
# given an infinite number of quarters, dimes, nickels, and pennies
# write code to calculate the number of ways of representing n cents

# KIND OF MAKES SENSE BUT A LITTLE HARD TO FOLLOW
# I PREFER HASHMAPS OVER ARRAYS FOR CACHING
def coins(n, denoms):
    map = [[]]
    def make_change_helper(total, denoms, index, map):
        # check map for prior results
        if map[total][index] > 0:
            return map[total][index]
        coin = denoms[index]
        if index == len(denoms) - 1:
            remaining = total % coin
            return 1 if remaining == 0 else 0
        
        numberOfWays = 0
        amount = 0
        while amount <= total:
            numberOfWays += make_change_helper(total - amount, denoms, index + 1, map)
            amount += coin

        # update map
        map[total][index] = numberOfWays

        return numberOfWays

# 8.12 eight queens
# write an algo to print all the ways of arranging 8 queens on an 8x8 chess board such that none of them
# share the same row, column, or diagonal
def eight_queens(row, columns, results):
    # check if the given row and column are a valid spot to put a queen
    # we dont need to check row because we already are iterating through the rows 1 by 1
    # so its not possible they would be in the same row
    def check_valid(columns, row1, col1):
        for row2 in range(row1):
            col2 = columns[row2]
            # check if same column
            if col1 == col2:
                return False
            
            columnDistance = abs(col2 - col1)
            rowDistance = row1 - row2
            # check if they are on the same diagonal
            if columnDistance == rowDistance:
                return False
        return True

    if row == 8: results.append(columns.copy())
    else:
        for c in range(8):
            if check_valid(columns, row, c):
                columns[row] = columns
                eight_queens(row + 1, columns, results)

# 8.13 stack of boxes
# given a stack of n boxes with widths w, heights h, and depths d.
# the boxes cannot be rotated and can only stack on top of one another if each box in the stack
# is larger than the box above it in all dimensions
# implement a method to compute the height of the tallest possible stack
def stack_of_boxes(boxes):
    """
    this solution requires class implementation of boxes in ordered to compare them
    revisit this problem later
    2 ways to do this
        first way is to use caching and see what the biggest stack you can build with box n as the base
        second way is to make a choice at each step to put the box in the stack or to not put the box in the stack
    """
    pass

# 8.14 boolean evaluation
# given a boolean expression consisting of 0,1,&,|, and ^ and a desire result value boolean, implement a function to count
# the number of ways of parenthesizing the expression such that it evaluates to result

# THIS IS FROM THE BOOK
# I DONT REALLY UNDERSTAND THIS
def boolean_expression():
    """
    the solution is to complex to explain here concisely
    go to page 368
    """
    pass
