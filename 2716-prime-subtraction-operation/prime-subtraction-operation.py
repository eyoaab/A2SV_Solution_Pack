class Solution:
    def primeSubOperation(self, nums: list[int]) -> bool:
       
        maxElement = max(nums)
        
        store = [True] * (maxElement + 1)
        store[1] = False
        
        for i in range(2, int((maxElement + 1) ** 0.5) + 1):
            if store[i]:
                for j in range(i * i, maxElement + 1, i):
                    store[j] = False
        
        curr = 1
        i = 0
        while i < len(nums):
            difference = nums[i] - curr
            
            if difference < 0:
                return False
            
            if store[difference] == True or difference == 0:
                i += 1
                curr += 1
            else:
                curr += 1
                
        return True