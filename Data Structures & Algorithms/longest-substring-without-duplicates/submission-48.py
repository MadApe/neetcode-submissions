class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        seen = set()
        longest_len = 0
        current_len = 0

        if len(s) == 1:
            return 1

        for i in range(len(s) - 1):
            seen = set()
            seen.add(s[i])
            current_len = 1

            for j in range(i + 1, len(s)):
                c = s[j]
                if c in seen:
                    longest_len = max(current_len, longest_len)

                    break
                
                current_len += 1
                longest_len = max(current_len, longest_len)
                seen.add(c)

        longest_len = max(current_len, longest_len)

        return longest_len
