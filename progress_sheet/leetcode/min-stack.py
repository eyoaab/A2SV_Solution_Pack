class MinStack:

    def __init__(self):
        self.ministack=[]
        
    def push(self, val: int) -> None:
        self.ministack.append(val)

    def pop(self) -> None:
        self.ministack.pop()
        
    def top(self) -> int:
        return self.ministack[-1]
        

    def getMin(self) -> int:
        return min(self.ministack)
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()