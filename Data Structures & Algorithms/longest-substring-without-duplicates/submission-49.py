class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        longest_len = 0
        l = 0
        r = 0

        for r in range(len(s)):
            c = s[r]

            if c in seen:
                l = max(seen[c] + 1, l)
            
            seen[c] = r
            current_len = r-l+1
            longest_len = max(longest_len, current_len)
        
        return longest_len
