class Solution:
    def reverse(self, x: int) -> int:
        reversed = 0
        sign = -1 if x < 0 else 1

        x = abs(x)

        # remove each digit from the right of x and stick it on reversed
        # moving the current value of reversed to the left by a factor of 10
        # then adding the right most digit of x
        while x > 0:
            reversed = (reversed * 10) + (x % 10)
            x //= 10

        reversed *= sign

        if reversed < -2**31 or reversed > 2**31:
            return 0

        return reversed

        