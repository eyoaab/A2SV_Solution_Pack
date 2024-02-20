class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        total=0
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]<target:
                    total+=1
        return total            

        