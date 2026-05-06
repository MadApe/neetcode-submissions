class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        freq = defaultdict(int)
        for c in s1:
            freq[c] = freq[c] + 1


        while r < len(s2):
            c2 = s2[r]

            if c2 not in freq:
                while l <= r:
                    c1 = s2[l]
                    if c1 in freq:
                        freq[c1] += 1

                    l += 1

                r += 1
                l = r
            else:
                if freq[c2] > 0:
                    freq[c2] -= 1

                    if r - l + 1 == len(s1):
                        return True

                    r += 1
                else:
                    while l < r and s2[l] != c2:
                        if s2[l] in freq:
                            freq[s2[l]] += 1
                        l += 1
                    r += 1
                    l += 1

        return False

