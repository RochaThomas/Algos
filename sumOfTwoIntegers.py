# morning algos
# neetcode Sum Of Two Integers

class Solution:
    def getSum(self, a, b):

        # solution too slow but has video
        # while b != 0:
        #     temp = (a & b) << 1
        #     a = a ^ b
        #     b = temp
        
        # return a

        # viable solution
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if add(~a, 1) == b:  # -a == b
                return 0
            if add(~a, 1) < b:  # -a < b
                return add(~add(add(~a, 1), add(~b, 1)), 1)  # -add(-a, -b)

        return add(a, b)  # a*b >= 0 or (-a) > b > 0

    print(getSum(1, 2))