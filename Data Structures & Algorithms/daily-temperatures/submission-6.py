class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        results = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while len(stack) > 0 and t > temperatures[stack[-1]]:
                si = stack.pop()
                results[si] = i - si

            stack.append(i)

        return results

