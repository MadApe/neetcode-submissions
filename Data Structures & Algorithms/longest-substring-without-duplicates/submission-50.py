class Solution:
    # moving window with hash map
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}  # for a char (k), stores the largest index in s (v) where the char occurred
        longest_len = 0
        l = 0
        r = 0

        # iterate over the characters in s
        for r in range(len(s)):
            c = s[r]

            # if we've this character then move the left ptr toward the right past where
            # the character was seen
            if c in seen:
                l = max(seen[c] + 1, l)
            
            seen[c] = r  # update the location where the character was seen
            current_len = r-l+1  # calculate the length of the window
            longest_len = max(longest_len, current_len)  # determine if the window size is a new max
        
        return longest_len
