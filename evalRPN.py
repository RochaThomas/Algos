# morning algos
# neetcode evaluate reverse polish notation


def evalRPN(tokens):
    stack = []

    for c in tokens:
        match c:
            case "+":
                stack.append(stack.pop() + stack.pop())
            case "-":
                b, a = stack.pop(), stack.pop()
                stack.append(a - b)
            case "*":
                stack.append(stack.pop() * stack.pop())
            case "/":
                b, a = stack.pop(), stack.pop()
                stack.append(int(a / b))
            case _:
                stack.append(int(c))
    return stack[0]


print(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))