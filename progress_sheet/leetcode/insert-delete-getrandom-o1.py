class RandomizedSet:

    def __init__(self):
        self.se=set()
        self.ans=list()
        

    def insert(self, val: int) -> bool:
        if val not in self.se:
            self.se.add(val) 
            return True
        return False    
        

    def remove(self, val: int) -> bool:
        if val in self.se:
            self.se.remove(val)
            return True
        return False

    def getRandom(self) -> int:
         
        return random.choice( list(self.se))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()