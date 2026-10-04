class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # iterate through the temperatures
        # Push the temperature to the stack
        # Check if the current temperature is larger than the bottom of the stack
        # If so remove the bottom one from the stack
        # Have a counter increment everytime the next temp isnt higher

        stack = []
        output = [0] * len(temperatures)
        i = 0

        # Iterate through the temperatures
        while i < len(temperatures):
            # If the temp is less than the top of the stack
            # Push the current temp to the stack
            # increment
            if len(temperatures) > 0 and len(stack) > 0 and temperatures[i] <= stack[-1][0]:
                stack.append((temperatures[i], i)) 
                i = i + 1
            elif len(stack) == 0:
                stack.append((temperatures[i], i))
                i = i + 1
            else:
                # The current temp is higher than the top of the stack
                # Find the distance to the day at the top of the stack
                # and append to output array at its day index
                distance = i - stack[-1][1]
                output[stack[-1][1]] = distance

                # Pop the top of the stack
                stack.pop()

        for item in stack:
            index = item[1]
            output[index] = 0

        return output

    # Iterate backwards through the List
