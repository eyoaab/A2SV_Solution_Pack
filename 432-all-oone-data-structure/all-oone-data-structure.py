class AllOne:

    def __init__(self):
        self.store = defaultdict(int)
        self.value = defaultdict(set)

    def inc(self, key: str) -> None:
        if key in self.store:
            previousCount = self.store[key]
            self.value[previousCount].remove(key)

            self.value[previousCount + 1].add(key)
            self.store[key] += 1
        else:
            self.store[key] = 1
            self.value[1].add(key)


        

    def dec(self, key: str) -> None:
         if key in self.store:
            previousCount = self.store[key]
            self.value[previousCount].remove(key)
            
            if previousCount == 1:
                del self.store[key] 
            else:
                self.value[previousCount - 1].add(key)
                self.store[key] -= 1
        

    def getMaxKey(self) -> str:
        if self.store.values():
            maxIndex = max(self.store.values())
            return list(self.value[maxIndex])[0]

        return ''     

        
        

    def getMinKey(self) -> str:
        if self.store.values():
            maxIndex = min(self.store.values())
            return list(self.value[maxIndex])[0]

        return ''     

        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()