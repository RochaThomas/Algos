# morning algos
# neetcode Plus One

class Solution:
    def plusOne(self, digits):
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            curr = digits[i] + carry
            digits[i] = curr % 10
            if curr < 10:
                return digits
        return [carry] + digits


    print(plusOne([1,2,3]))