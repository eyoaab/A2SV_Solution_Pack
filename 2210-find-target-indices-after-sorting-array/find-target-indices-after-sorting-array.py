class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()

        answer = [index for index,num in enumerate(nums) if target == num]
        return answer




        