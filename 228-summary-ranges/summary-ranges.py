class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []

        output = []
        index = 0
        while index < len(nums):
            start = nums[index] 
            while index + 1 < len(nums) and nums[index] + 1 == nums[index + 1]:
                index += 1
            
            if start == nums[index]:
                output.append(f"{start}")
            else:
                output.append(f"{start}->{nums[index]}")
            
            index += 1
        
        return output