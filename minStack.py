# morning algos
# neetcode min stack

class MinStack:
    def __init__(self):
        self.stack = []
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min:
            self.min = val

    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min:
            newMin = float('inf')
            for v in self.stack:
                newMin = min(newMin, v)
            self.min = newMin

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min