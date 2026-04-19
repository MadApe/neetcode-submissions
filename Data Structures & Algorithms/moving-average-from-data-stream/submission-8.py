class MovingAverage:
    # circular buffer
    def __init__(self, size: int):
        self.size = size
        self.buffer = [0] * size
        self.head = 0
        self.count = 0
        self.running_sum = 0

    def next(self, val: int) -> float:
        self.running_sum -= self.buffer[self.head]
        self.running_sum += val

        self.buffer[self.head] = val
        self.head = (self.head + 1) % self.size

        if self.count < self.size:
            self.count += 1

        return self.running_sum / self.count


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
