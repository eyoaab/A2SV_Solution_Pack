class CustomStack:

    def __init__(self, maxSize: int):
        self.lis=list()
        self.ma=maxSize

    def push(self, x: int) -> None:
        if len(self.lis)<self.ma:
            self.lis.append(x)

        

    def pop(self) -> int:
        if self.lis:
            k=self.lis.pop()
            return k
        return -1    
        

    def increment(self, k: int, val: int) -> None:  
            for i in range(k):
                if len(self.lis)>i:
                    self.lis[i]+=val
                else:
                    break    
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)