# morning algos
# neetcode car fleet

# pseudo
# if for car 2 position + speed * n >= car 1 position + speed * n then thats a fleet
# run a loop to increment n as long ass position + speed * n is less than target
# 
# handling the stack is trickier...
# put them all in a stack where each index is a pair of [position, speed]
# iterate through the stack?
# pop until there is a new fleet
# everytime you enter into a while loop to pop the "fleet" increment result count by 1 


# neetcode solution
# rewatch video if you need a reminder
# but comments below should be enough

def carFleet(target, position, speed):
    # creates an array of pairs
    pair = [[p, s] for p, s in zip(position, speed)]

    stack = []
    # sorting the array of pairs in reverse order by position 
    for p, s in sorted(pair)[::-1]:
        # calculating and appending the time it takes a car to reach destination

        # in leetcode stack.append(float((target - p)) / s)
        stack.append((target - p) / s)

        # if len(stack) >= 2 is checking that there are at least 2 elements in the stack
        # if it was just 1 car you wouldn't need to do anything

        # second half of the if statement is checking if the time of the car in the back is shorter than the time of the car in the front
        # if it is then they form a fleet
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()

    return len(stack)

print(carFleet(10, [6,8], [3,2]))