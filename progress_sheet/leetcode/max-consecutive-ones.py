class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len=0
        i=0
        k=0
        while i<len(nums):
            if nums[i]==1:
                k+=1
            else:
                k=0
            max_len=max(max_len,k)
            i+=1

        return max_len       

            

       
        
        return max_len