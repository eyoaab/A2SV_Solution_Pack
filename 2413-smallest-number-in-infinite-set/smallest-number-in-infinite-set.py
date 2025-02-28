class SmallestInfiniteSet:
    def __init__(self):
        self.heap = [] 
        self.visited = set()
        self.smallest = 1  

    def popSmallest(self) -> int:
        if self.heap:
            num = heappop(self.heap)  
            self.visited.remove(num)
            return num
        else:
            num = self.smallest
            self.smallest += 1  
            return num

    def addBack(self, num: int) -> None:
        if num < self.smallest and num not in self.visited:
            heappush(self.heap, num)
            self.visited.add(num)
