def doMath(op: str, v1: int, v2: int) -> int:
    val = 0
    if op == '+':
        val = v1 + v2
    if op == '-':
        val = v1 - v2
    if op == '*':
        val = v1 * v2
    if op == '/':
        val = int(v1 / v2)

    return val


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        symbols = ['+','-','*','/']

        if len(tokens) == 1:
            return int(tokens[0])

        for t in tokens:
            if t not in symbols:
                stack.append(int(t))
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                res = doMath(t, v1, v2)
                stack.append(res)

        return stack.pop()
