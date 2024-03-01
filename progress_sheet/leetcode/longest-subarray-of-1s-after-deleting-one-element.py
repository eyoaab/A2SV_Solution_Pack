class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero=0
        ones=0
        max_one=0
        l=0
        for i in range(len(nums)):
            if nums[i]==0:
                zero+=1
                if zero>1:
                    while nums[l]!=0:
                        ones-=1
                        print(ones,zero)
                        l+=1
                    l+=1    
                    zero-=1
            else:
                ones+=1
                max_one=max(max_one,ones)            
        #max_one=max(max_one,len(nums)-l-zero)
        if max_one==len(nums):
            return max_one-1
        return max_one     
                

        