class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans=[]
        if target not in nums:
            return [-1,-1]    
        ans.append(nums.index(target))
        nums=nums[::-1]
        ans.append(len(nums)-nums.index(target)-1)
        return ans

        