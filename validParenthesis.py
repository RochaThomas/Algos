# morning algos
# neetcode valid parenthesis


# neetcode solution
# using an array as a stack
# furthering this...
# follow up: how would you do this for different characters
# for example... A is open and a is close, B is open and b is closed ---> through the rest of the alphabet
# use a for loop to set up a hashmap of closed to open characters and run the below logic, this should work

def isValid(s):
    
    stack = []
    closeToOpen = {")":"(", "]":"[","}":"{"}

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)
    
    return True if not stack else False

print(isValid("()"))