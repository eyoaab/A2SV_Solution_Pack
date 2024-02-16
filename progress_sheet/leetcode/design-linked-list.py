class MyLinkedList:

    def __init__(self):
        self.store=[]
        

    def get(self, index: int) -> int:
        if 0<=index <len(self.store):
            return self.store[index]
        return -1    
        

    def addAtHead(self, val: int) -> None:
        self.store=[val]+self.store
        

    def addAtTail(self, val: int) -> None:
        self.store.append(val)
        
    def addAtIndex(self, index: int, val: int) -> None:
        if index==0:
            self.addAtHead(val)
        elif index==len(self.store):
            self.addAtTail(val)
        elif 0 < index < len(self.store):
            self.store=self.store[:index]+[val]+self.store[index:]     

        
    def deleteAtIndex(self, index: int) -> None:
            if 0 <= index < len(self.store) : 
                self.store = self.store[:index] + self.store[index+1:]
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)