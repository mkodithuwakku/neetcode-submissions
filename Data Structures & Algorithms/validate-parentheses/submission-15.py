class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
    
            if char == ")" and len(stack) > 0:
                if stack[-1] == "(":
                    stack.pop()
                else:
                    return False
            
            elif char == "}" and len(stack) > 0 :
                if stack[-1] == "{":
                    stack.pop()
                else:
                    return False
            
            elif char == "]" and len(stack) > 0:
                if stack[-1] == "[":
                    stack.pop()
                
                else:
                    return False
            
            else:
                stack.append(char)
            
            
        if len(stack) > 0:
            return False
        else:
            return True
        

