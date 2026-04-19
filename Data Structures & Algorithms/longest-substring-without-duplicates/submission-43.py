class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # brute force
        seen = {}
        longest_len = 0
        current_len = 0

        if len(s) == 1:
            return 1

        for i in range(len(s) - 1):
            seen = {s[i]: True}
            current_len = 1
            print(f"s[i]={s[i]}")

            for j in range(i + 1, len(s)):
                c = s[j]
                print(f"s[j]={c}")
                if c in seen:
                    print(f"j=[{j}] current_len={current_len}")
                    longest_len = max(current_len, longest_len)
                    print(f"j=[{j}] longest_len={longest_len}")

                    break
                
                current_len += 1
                longest_len = max(current_len, longest_len)
                seen[c] = True

            print(f"i=[{i}] current_len={current_len}")
            print(f"i=[{i}] longest_len={longest_len}")

        print(f"current_len={current_len}")
        print(f"longest_len={longest_len}")
        longest_len = max(current_len, longest_len)

        return longest_len
