class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        referance={}
        for i in range(len(nums)):
            referance[nums[i]]=i

        for key,val in operations:
            ind=referance[key]
            referance.pop(key)
            nums[ind]=val
            referance[val]=ind


        return nums              
        