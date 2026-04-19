class Solution:
    def isValid(self, s: str) -> bool:
        result = True
        p = ""
        for i in range(len(s)):
            c = s[i]
            if c in ('(', '[', '{'):
                p += c
            elif c in (')', ']', '}'):
                if c == ')':
                    if len(p) == 0 or p[len(p) - 1] != '(':
                        return False
                if c == ']':
                    if len(p) == 0 or p[len(p) - 1] != '[':
                        return False
                elif c == '}':
                    if len(p) == 0 or p[len(p) - 1] != '{':
                        return False
                p = p[:len(p) - 1]
            
            # print(f"c={c}, p={p}")

        if p:
            result = False

        return result
