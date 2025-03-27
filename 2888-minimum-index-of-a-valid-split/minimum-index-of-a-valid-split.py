class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        def find(arr):
            store = None
            count = 0
            
            for num in arr:
                if count == 0:
                    store = num
                    count = 1
                elif num == store:
                    count += 1
                else:
                    count -= 1
            
            count = sum(1 for num in arr if num == store)
            return store if count > len(arr) // 2 else None

        dominant = find(nums)
        
        if dominant is None:
            return -1
        
        left = 0
        total_dominant = sum(1 for num in nums if num == dominant)
        
        for i in range(len(nums) - 1):
            if nums[i] == dominant:
                left += 1
            
            left_subarray = left
            right_subarray = total_dominant - left
            
            if (left_subarray > (i + 1) // 2 and 
                right_subarray > (len(nums) - i - 1) // 2):
                return i
        
        return -1
        