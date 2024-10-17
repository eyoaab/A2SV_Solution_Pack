class RandomizedCollection:
    def __init__(self):
      
        self.vals = [] 
        self.indices = {} 

    def insert(self, val: int) -> bool:
        
        self.vals.append(val)
        if val in self.indices:
            self.indices[val].add(len(self.vals)-1) 
            return False
        else:
            self.indices[val] = {len(self.vals)-1} 
            return True

    def remove(self, val: int) -> bool:
        if val not in self.indices:
            return False
        
        index = self.indices[val].pop() 
        last_val = self.vals[-1] 
        if index != len(self.vals)-1: 
            self.vals[index] = last_val 
            self.indices[last_val].discard(len(self.vals)-1)
            self.indices[last_val].add(index) 
        
        self.vals.pop() 
        if not self.indices[val]: 
            del self.indices[val] 

        return True

    def getRandom(self) -> int:
     
        return random.choice(self.vals) 