class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}  # count the frequency of the characters in the current window
        res = 0     # the max string length with <= k replacements

        l = 0     # left of window
        maxf = 0  # highest frequency of most frequent char in the window
        
        # step through the string
        for r in range(len(s)):
            # increment the current character's frequency
            count[s[r]] = 1 + count.get(s[r], 0)

            # determine if the current character is the most frequent
            maxf = max(maxf, count[s[r]])

            #
            # if the size of the window minus the most frequent character is more than k
            # shrink the window from the left, and decrement the count of each character
            # as we shrink the window
            #
            # window_size = r - l + 1
            # num_replacements = window_size - maxf 
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1

            # set the max comparing the current max to the current string length
            res = max(res, r - l + 1)

        return res