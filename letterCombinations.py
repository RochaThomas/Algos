# morning algos
# neetcode Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        res = []
        digitsToChar = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }

    print(letterCombinations("23"))