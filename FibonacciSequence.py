# interview prep practice
# Fibonacci Sequence
def fibSeq(n):
    res = [0, 1]
    prev, curr = res[0], res[1]
    for i in range(n):
        temp = prev + curr
        res.append(temp)
        prev = curr
        curr = temp
    return res
    
def recFibSeq(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return recFibSeq(n - 2) + recFibSeq(n - 1)

print(recFibSeq(n=10))