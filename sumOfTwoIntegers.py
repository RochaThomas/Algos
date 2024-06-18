# morning algos
# neetcode Sum Of Two Integers

class Solution:
    def getSum(self, a, b):
        while b != 0:
            temp = (a & b) << 1
            a = a ^ b
            b = temp
        return a

    print(getSum(1, 2))