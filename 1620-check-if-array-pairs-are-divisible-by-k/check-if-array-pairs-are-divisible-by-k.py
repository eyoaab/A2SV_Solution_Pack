class Solution:
    def canArrange(self, nums: List[int], k: int) -> bool:

        for i in range(len(nums)):
            nums[i] %= k

        count =  Counter(nums) 
        if count[0]%2 !=0:
            return False

        for num in set(nums):
            comp = k-num
            if num !=0 and ((not comp in count) or count[comp] != count[num]):
                return False

        return True        

           

         
        