# morning algos
# neetcode evaluate reverse polish notation


def evalRPN(tokens):
    nums = []
    for c in tokens:
        if c == "+":
            nums.append(nums.pop() + nums.pop())
        elif c == "-":
            n1, n2 = nums.pop(), nums.pop()
            nums.append(n2 - n1)
        elif c == "*":
            nums.append(nums.pop() * nums.pop())
        elif c == "/":
            n1, n2 = nums.pop(), nums.pop()
            nums.append(int(n2 / n1))
        else:
            nums.append(int(c))

    return nums[0]


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))