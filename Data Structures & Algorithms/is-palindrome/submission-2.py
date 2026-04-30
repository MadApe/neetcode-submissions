class Solution:
    def isPalindrome(self, s: str) -> bool:
        norm_s = re.sub(r'[^A-z0-9]', '', s.lower())
        rev_s = ''

        for c in norm_s[::-1]:
            rev_s += c

        return norm_s == rev_s