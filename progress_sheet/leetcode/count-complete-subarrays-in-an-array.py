class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        unique=len(set(nums))
        n=len(nums)
        counter=0
        for i in range(n):
            current=set()
            for j in range(i,n):
                current.add(nums[j])
                if len(current)==unique:
                    counter+=n-j
                    break
        return counter



            
        