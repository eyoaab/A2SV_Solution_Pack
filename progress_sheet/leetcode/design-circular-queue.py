class MyCircularQueue:

    def __init__(self, k: int):
        self.de=deque()
        self.k=k

    def enQueue(self, value: int) -> bool:
        if self.k==len(self.de):
            return False
        self.de.appendleft(value)
        return True

    def deQueue(self) -> bool:
        if self.de:
            self.de.pop()
            return True
        return False    
        

    def Front(self) -> int:
        if not self.de:
            return -1
        return self.de[-1]    

        

    def Rear(self) -> int:
        if not self.de:
            return -1
        return self.de[0]
        

    def isEmpty(self) -> bool:
        return len(self.de)==0 
        

    def isFull(self) -> bool:
        return self.k==len(self.de)
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()