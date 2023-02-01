
# morning algos
# neetcode encode and decode strings


"""
below is neetcode's solution which I like better
time: O(n)
space: O(n) for decode and O(1) for encode

my original solution used a salt
encode used a .join method or just used a for loop to iterate through and add the salt
decode was similar to the solution below
    I used a loop and used a if statement to check if the string from i to i + length of the salt
    was equal to the salt, if it was i would push the current string i was building to the result,
    add the length of the salt to i, reset the current string variable to an empty string, and set
    the beginning index variable to i

    very similar but i liked how neetcode's solution incorporated the length of the strings before
    the salt
"""
class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        res = ""
        for s in strs:
            res += len(s) + '#' + s
        return res

    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != '#':
                j += 1
            length = int(str[i:j])
            res.append(str[j + 1 : j + 1 + length])
            i = j + 1 + length

        return res


# https://www.lintcode.com/problem/659/
