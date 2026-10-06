class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        # push elements to the stack
        # when an operand is encountered
        # use the previous two elements of the stack to compute it
        # push the result to the stack and pop the other two

        stack = []
        for elem in tokens:

            if elem == "+":
                num1 = int(stack[-1])
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()

                result = num1 + num2
                stack.append(result)
            elif elem == "-":
                num1 = int(stack[-1])
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()

                result = num2 - num1
                stack.append(result)

            elif elem == "*":
                num1 = int(stack[-1])
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()

                result = num2 * num1
                stack.append(result)

            elif elem == "/":
                num1 = int(stack[-1])
                stack.pop()
                num2 = int(stack[-1])
                stack.pop()

                result = num2 / num1
                stack.append(result)
            
            else:
                stack.append(int(elem))
            
        return int(stack[-1])