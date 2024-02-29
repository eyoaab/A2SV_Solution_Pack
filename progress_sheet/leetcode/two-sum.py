class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        referance={}

        for i in range(len(nums)):

            if nums[i] in referance:
                return [referance[nums[i]],i]
            referance[target-nums[i]]=i    

        return []        
        