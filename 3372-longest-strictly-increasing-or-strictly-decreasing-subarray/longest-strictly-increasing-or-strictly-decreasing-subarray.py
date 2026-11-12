class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_increasing = 1
        cur = 1
        for  i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                cur +=1
                max_increasing = max(max_increasing,cur)
            else:
                cur = 1

        max_decrease = 1
        cur = 1
        for  i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                cur +=1
                max_decrease = max(max_decrease,cur)
            else:
                cur = 1        

        return max(max_decrease,max_increasing)            
           
    