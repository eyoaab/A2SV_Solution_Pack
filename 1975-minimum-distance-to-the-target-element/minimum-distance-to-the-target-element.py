class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float('inf')
        
        for i in range(start,-1,-1):
            if nums[i] == target:
                ans = min(ans,start - i)
                break

        for i in range(start,len(nums)):
            if (nums[i] == target):
                ans = min(ans,i - start)
                break

        return ans                