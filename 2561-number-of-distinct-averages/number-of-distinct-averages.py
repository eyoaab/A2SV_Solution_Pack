class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        
        N = len(nums)
        store = set()
        
        
        left = 0
        right = N - 1
        
        while left < right:
           
            N -= 2  
            
            average = (nums[left] + nums[right])/ 2
            store.add(average)
            
            left += 1
            right -= 1
        
        return len(store)
