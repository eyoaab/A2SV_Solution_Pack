class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:         
        answer=[0]*len(nums)
        i=0
        for j in range(len(nums)):
            if( nums[j]<pivot):
                answer[i]=nums[j]
                i+=1
    
        for j in range(len(nums)):
            if( nums[j]==pivot):
                answer[i]=nums[j]
                i+=1
        for j in range(len(nums)):
            if( nums[j]>pivot):
                answer[i]=nums[j]
                i+=1
    
        return answer


       