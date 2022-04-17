class MyQueue:

    def __init__(self):
        self.stack=list()
        self.stack2=list()

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        while self.stack:
            self.stack2.append(self.stack.pop())
        print(self.stack2)
        s1=self.stack2.pop()
        while self.stack2:
            self.stack.append(self.stack2.pop())
        return s1

    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        if len(self.stack)==0:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()