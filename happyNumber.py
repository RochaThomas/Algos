# morning algos
# neetcode Happy Number

class Solution:
    def isHappy(self, n):
        visit = set()

        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)

            if n == 1:
                return True
        
        return False

    def sumOfSquares(self, num):
        output = 0

        while num:
            digit = num % 10
            digit = digit ** 2
            output += digit
            num = num // 10
        
        return output

    print(isHappy(19))