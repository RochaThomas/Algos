# cracking the coding interview
# chapter 10 searching and sorting

# interview questions

# 10.1 sorted merge
# merge two sorted arrays where array a has a long enough buffer at the end to fit array b
# start at the last number of each array, compare and add to end of array a

# 10.2 group anagram
# sort a list of string so that all anagrams of each other are next to one another
# make a hashmap where key is a sorted string and value is an array of strings, add string to array if it matches
# key when sorted, return hashmap values

# 10.3 search in rotated array
# given a sorted array that has been rotated x times find a target value
# the books solution is subpar and unclear, watch neetcode video for this problem
# just a modified binary search

# 10.4 sorted search, no size
# given a sorted array like data structure that does not have a method to get the length and only has a method
# to get the the ith value given i, find a target value
# estimate size by increasing by 2 exponentially until you hit a null value
# then run binary search

# 10.5 sparse search
# given a sorted array of strings interspersed with empty strings write a method to search for a string
# just do binary search comparing string, if you hit an empty string search for the nearest nonempty

# 10.6 sort big file
# imagine a 20 gb file with 1 string per line how do you sort the file
# external sort... search this up

# 10.7 missing int
# given an input file with 4 billion non neg ints, write an algo that will give you a int that is not in the file
# you only have 1 gb of space
# i do not understand the solution to this

# 10.8 find duplicates
# given an array with nums 1 - N where N < 32,000 and only 4 kb memory
# write an algo to print all the duplicate elements in the array
# i do not understand this solution, look up how to create and use bit vectors

# 10.9 sorted matrix search
# given an m x n matrix where each row and col is sorted in ascending order write an algorithm to find an element
# basically a double binary search
# binary search 1 checks to see if target is in range of middle array
# if less than lowest of middle then search lesser rows
# if greater than greatest of middle then search greater rows
# if in the rows range, do a normal binary search
# jk this problem is different, it isn't specifying that the end of the previous row is less than the beginning of the next row
# so partition the matrix into 4 quadrants based on the middle value and recursively search
# maybe find a solution to this

# 10.10 rank from stream
# while taking in a stream of integers, write a method that will given you the rank of an integer x
# where the rank is how many read ints are less than or equal to x
# use a binary search tree where every node keeps track of the size of its left branch
# so upon insertion and search, when you move right you just add 1 to the size of left branch stored in the node

