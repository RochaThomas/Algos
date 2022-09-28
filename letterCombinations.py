# morning algos
# neetcode Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, curr):
            if len(curr) == len(digits):
                res.append(curr[:])
                return

            for c in digitToChar[digits[i]]:
                backtrack(i + 1, curr + c)

        if digits:
            backtrack(0, "")
        return res


    print(letterCombinations("23"))