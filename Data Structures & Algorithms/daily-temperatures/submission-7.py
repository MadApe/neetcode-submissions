class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # holds indices into temperatures
        results = [0] * len(temperatures)  # initialize the results

        # iterate over the temperatures
        for current_index, current_temp in enumerate(temperatures):
            # while current temp is greater than the temp associated with the last index on the stack
            while len(stack) > 0 and current_temp > temperatures[stack[-1]]:
                # remove the last item from the stack - which is the index to update
                index_to_update = stack.pop()

                # set the results value for the index to update to the # days until higher temp (current_index - index_to_update)
                results[index_to_update] = current_index - index_to_update

            # append the current value to the stack in every case
            stack.append(current_index)

        return results

