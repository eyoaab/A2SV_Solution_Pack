class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #return bisect_left(nums,target)
        left=0
        right=len(nums)-1
        while left <= right:
            mid=(left+right)//2
            if nums[mid] <= target:
                left=mid+1
            else:
                right=mid-1

               

        if target in nums:
            return left-1
            
        return left      

        