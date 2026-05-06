from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        r = l = 0
        min_len = float('inf')
        min_l = None
        min_r = None

        t_freq = defaultdict(int)
        for c in t:
            t_freq[c] += 1

        window_freq = defaultdict(int)

        needed_match_len = len(t_freq)
        have_match_len = 0

        for r in range(len(s)):
            c = s[r]
            window_freq[c] += 1
            if c in t_freq and window_freq[c] == t_freq[c]:
                have_match_len += 1

            while have_match_len == needed_match_len:
                if (r - l) < min_len:
                    min_l = l
                    min_r = r
                    min_len = r - l

                window_freq[s[l]] -= 1
                if s[l] in t_freq and window_freq[s[l]] < t_freq[s[l]]:
                    have_match_len -= 1
                
                l += 1

        if min_l is None or min_r is None:
            return ""
        
        return s[min_l:min_r+1]
                

