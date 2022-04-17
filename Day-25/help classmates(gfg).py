class MinStack:

    def __init__(self):
        self.stack=list()
        self.smin=list()
  
    def push(self, val: int) -> None:
        if len(self.smin)==0:
            self.smin.append(val)
        else:
            self.smin.append(min(val,self.smin[-1]))
            
        self.stack.append(val)
        

    def pop(self) -> None:

        self.stack.pop()
        self.smin.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smin[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()