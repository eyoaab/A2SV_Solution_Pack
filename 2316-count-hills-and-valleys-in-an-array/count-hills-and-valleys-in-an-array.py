class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        store = [nums[0]]
        ans = 0

        for num in nums:
            if num != store[-1]:
                store.append(num)
         
        for i in range(1,len(store) - 1):
            ans += store[i-1] < store[i] > store[i + 1]  # hill
            ans += store[i-1] > store[i] < store[i + 1]   #vally 

        return ans      
