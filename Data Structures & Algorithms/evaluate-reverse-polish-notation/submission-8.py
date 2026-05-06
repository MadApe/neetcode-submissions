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

    print(f"Performed: {v1} {op} {v2} = {val}")
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
                print(f"append {int(t)} to the stack to be: {stack}")
            else:
                v2 = stack.pop()
                v1 = stack.pop()
                res = doMath(t, v1, v2)
                stack.append(res)
                print(f"append {res} to the stack to be: {stack}")

        return stack.pop()
