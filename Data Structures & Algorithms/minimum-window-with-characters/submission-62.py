class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""
        
        # Pre-allocate arrays for 128 ASCII characters
        t_freq = [0] * 128
        window_freq = [0] * 128
        
        # Use unique_chars to track how many characters in T we actually care about
        needed_matches = 0
        for char in t:
            idx = ord(char)
            if t_freq[idx] == 0:
                needed_matches += 1
            t_freq[idx] += 1

        l = 0
        have_matches = 0
        min_len = float('inf')
        res = (-1, -1)

        for r in range(len(s)):
            # Convert character to array index
            r_idx = ord(s[r])
            window_freq[r_idx] += 1
            
            # Check if this character now meets its frequency requirement in the window
            if t_freq[r_idx] > 0 and window_freq[r_idx] == t_freq[r_idx]:
                have_matches += 1
                
            while have_matches == needed_matches:
                # Update minimum window
                if (r - l + 1) < min_len:
                    min_len = r - l + 1
                    res = (l, r)
                
                # Shrink from the left
                l_idx = ord(s[l])
                if t_freq[l_idx] > 0 and window_freq[l_idx] == t_freq[l_idx]:
                    have_matches -= 1
                window_freq[l_idx] -= 1
                l += 1
                
        l, r = res
        return s[l : r + 1] if min_len != float('inf') else ""
