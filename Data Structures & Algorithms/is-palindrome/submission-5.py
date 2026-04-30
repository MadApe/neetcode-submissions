class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_s = re.sub(r'[^A-z0-9]', '', s.lower())
        return norm_s == norm_s[::-1]