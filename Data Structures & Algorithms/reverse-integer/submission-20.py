class Solution:
    def reverse(self, x: int) -> int:
        # brute force
        sign = -1 if x < 0 else 1
        x = abs(x)
        x_str = str(x)
        x_str.lstrip('-')
        print(f"x_str={x_str}, type={type(x_str)}")
        new_str = ""

        for i in range(len(x_str)):
            new_str += x_str[-i-1]

        print(f"new_str='{new_str}', type={type(new_str)}")

        v = int(new_str)
        v = v * sign
        print(f"v={v}")

        if v < -2**31 or v > 2**31:
            return 0

        return v