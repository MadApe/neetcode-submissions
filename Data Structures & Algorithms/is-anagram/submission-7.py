class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = dict()

        for c in s:
            if c in letters:
                letters[c] += 1
            else:
                letters[c] = 1

        for c in t:
            if c not in letters:
                return False
            else:
                letters[c] -= 1

        for k, v in letters.items():
            if v != 0:
                return False


        return True
