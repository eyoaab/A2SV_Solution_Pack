from collections import defaultdict

class FrequencyTracker:
    def __init__(self):
      
        self.dict = defaultdict(int)  
        self.frequency = defaultdict(int) 

    def add(self, number: int) -> None:
        temp = self.dict[number]
        
        self.dict[number] += 1

        self.frequency[temp] -= 1
        self.frequency[temp + 1] += 1

    def deleteOne(self, number: int) -> None:
      
        if number in self.dict:
            temp = self.dict[number]
  
            self.dict[number] -= 1        
            self.frequency[temp] -= 1
            if self.frequency[temp] == 0:
                del self.frequency[temp]
                
            if self.dict[number] == 0:
                del self.dict[number]
            else:
                self.frequency[temp - 1] += 1

    def hasFrequency(self, frequency: int) -> bool:
      
        return frequency in self.frequency and self.frequency[frequency] > 0

# Example usage:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
