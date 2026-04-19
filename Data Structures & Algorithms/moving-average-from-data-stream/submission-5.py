class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.values = []
        

    def next(self, val: int) -> float:
        self.values.append(val)
        if len(self.values) > self.window_size:
            self.values = self.values[1:]
        total = 0
        for n in self.values:
            total += n

        print(f"total = {total}, len(self.values) = {len(self.values)}")
        return total / len(self.values)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
