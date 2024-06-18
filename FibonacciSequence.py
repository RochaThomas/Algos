# interview prep practice
# Fibonacci Sequence
class Solution:
    def fibSeq(n):
        res = [0, 1]
        prev, curr = res[0], res[1]
        for i in range(n):
            temp = prev + curr
            res.append(temp)
            prev = curr
            curr = temp
        return res
    
    def reqFibSeq(n):
        pass

    print(fibSeq(10))