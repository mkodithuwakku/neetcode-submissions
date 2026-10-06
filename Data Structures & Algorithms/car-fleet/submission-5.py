class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        # zip the lists together
        # sort the car tuples by position
        # iterate through and find fleets
        # when a faster fleet is found push it to the stack
        # lenght of stack is the answer

        cars = list(zip(position,speed))
        cars.sort()

        stack = []

        for index in range(len(cars)-1,-1,-1):
            arrival = (target - cars[index][0])/cars[index][1]

            if len(stack) == 0:
                stack.append((cars[index][0],arrival))
            elif stack[-1][1] >= arrival:
                continue
            else:
                stack.append((cars[index][0],arrival))
        
        return len(stack)



        