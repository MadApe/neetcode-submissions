class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        
        # track the number of times each character in s1 occurs
        freq = defaultdict(int)     
        for c in s1:
            freq[c] = freq[c] + 1


        # loop through s2 string
        while r < len(s2):
            c2 = s2[r]  # current character in s2

            # if c2 is not in freq (e.g., not in s1) then we reset the left pointer
            # by point it to the right pointer.  In doing so, we need to reset the
            # freq for any characters we've seen to prepare for evaluating the next
            # window
            if c2 not in freq:
                while l <= r:
                    # move the left pointer to the right, resetting the freq of any
                    # characters in s1 as we go
                    c1 = s2[l]
                    if c1 in freq:
                        freq[c1] += 1

                    l += 1

                # now we move right one and let left = right (because we're starting a new window)
                r += 1
                l = r
            else:
                # the current character is in s1
                if freq[c2] > 0:
                    # we haven't seen this character more times than it shows up in s1 yet
                    freq[c2] -= 1

                    # if our window size is the len of s1 then we've found a permutation
                    if r - l + 1 == len(s1):
                        return True

                    r += 1
                else:
                    # the current character is in s1, but we've now seen it more times than
                    # it shows up in s1.  This means we need to move the left side of the window
                    # past the last time we saw the current character to make the window valid again,
                    # resetting the freq of any characters in s1 as we move
                    while l < r and s2[l] != c2:
                        if s2[l] in freq:
                            freq[s2[l]] += 1
                        l += 1
                    r += 1
                    l += 1

        return False

