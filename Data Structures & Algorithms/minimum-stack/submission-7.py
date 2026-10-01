class MinStack:

    def __init__(self):
        self.stack = []
        self.minNum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minNum is None or val < self.minNum:
            self.minNum = val
            print("changed min")
        else :
            print("no change")

    def pop(self) -> None:
        self.stack.pop()
        self.minNum = None
        

    def top(self) -> int:
        top = self.stack[-1]
        return top
        

    def getMin(self) -> int:
        if self.minNum is None and len(self.stack) > 0:
            self.minNum = 2 **31
            for num in self.stack:
                if num < self.minNum:
                    self.minNum = num
            return self.minNum
        else:
            return (self.minNum)
            
        
