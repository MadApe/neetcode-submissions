class Solution:
    def reverse(self, x: int) -> int:
        # brute force
        sign = -1 if x < 0 else 1
        x = abs(x)
        x_str = str(x)
        x_str.lstrip('-')
        new_str = ""

        # for i in range(len(x_str)):
        #     new_str += x_str[-i-1]
        new_str = x_str[::-1]

        v = int(new_str)
        v = v * sign

        if v < -2**31 or v > 2**31:
            return 0

        return v