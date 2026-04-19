class Solution:
    def isPalindrome(self, x: int) -> bool:
        # brutish
        s1 = str(x)
        l = 0
        r = len(s1) - 1
        while l < r:
            if s1[l] != s1[r]:
                return False
            l += 1
            r -= 1

        return True
