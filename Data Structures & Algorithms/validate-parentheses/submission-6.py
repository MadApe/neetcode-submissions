class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            elif c in (')', ']', '}'):
                if c == ')':
                    if len(stack) == 0 or stack.pop() != '(':
                        return False
                if c == ']':
                    if len(stack) == 0 or stack.pop() != '[':
                        return False
                elif c == '}':
                    if len(stack) == 0 or stack.pop() != '{':
                        return False
        
        if len(stack) > 0:
            return False
        else:
            return True

