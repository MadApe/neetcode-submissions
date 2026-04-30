class Solution:
    def isPalindrome(self, s: str) -> bool:
        ns = re.sub('[^A-z0-9]', '', s.lower())
        l = 0
        r = len(ns) - 1

        while l < r:
            if ns[l] != ns[r]:
                return False

            l += 1
            r -= 1
        
        return True
