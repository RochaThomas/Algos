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

        def backtrack(i, curr):
            if i >= len(digits):
                res.append(curr)
                return
            for letter in digitsToChar[digits[i]]:
                curr += letter
                backtrack(i + 1, curr)
                curr = curr[:-1]
        if not digits: return []
        backtrack(0, '')
        return res

    print(letterCombinations("23"))