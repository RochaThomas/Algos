# morning algos
# neetcode Happy Number

class Solution:
    def isHappy(self, n):
        cache = set()

        res = self.calc(n)
        while True:
            if res == 1:
                return True
            elif res in cache:
                return False
            else:
                cache.add(res)
                res = self.calc(res)
        
    def calc(self, num):
        res = 0
        while num > 0:
            digit = num % 10
            res += digit * digit
            num = num // 10
        return res

    print(isHappy(19))