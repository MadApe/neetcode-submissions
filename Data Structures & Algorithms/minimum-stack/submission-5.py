class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_i = len(self.min_stack) - 1
        if min_i < 0:
            min_val = val
        else:
            min_val = min(val, self.min_stack[min_i])
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[len(self.stack) - 1]

    def getMin(self) -> int:
        return self.min_stack[len(self.min_stack) - 1]
