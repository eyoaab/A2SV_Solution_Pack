class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def number_of_partition(p):
            count=1
            running_sum=0
            for i in range(len(nums)):
                if running_sum+nums[i]<=p:
                    running_sum+=nums[i]
                else:
                    count+=1
                    running_sum=nums[i]
            return count
        
     
        def binary_search(left,right):
            while left<=right:
                mid=left+(right-left)//2
                if number_of_partition(mid)<=k:
                    right=mid-1
                else:
                    left=mid+1
            return left
        first=max(nums)
        second=sum(nums)
       
        return  binary_search(first,second)

        