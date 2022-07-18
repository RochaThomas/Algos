# morning algos
# neetcode evaluate reverse polish notation


def evalRPN(tokens):
    stack = []
    operations = ["+", "-", "*", "/"]
    
    for t in tokens:
        if t in operations:
            temp = stack[-1]
            stack.pop()
            if t == "*":
                temp = stack[-1] * temp
            elif t == "/":
                # line below was originally just int() without the float but leetcode didn't get the same answer without the float()
                temp = int(float(stack[-1]) / temp)
            elif t == "+":
                temp = stack[-1] + temp
            elif t == "-":
                temp = stack[-1] - temp
            stack.pop()
            stack.append(temp)
        else:
            t = int(t)
            stack.append(t)

        print(stack)

    return stack[-1]

print(evalRPN(
["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))