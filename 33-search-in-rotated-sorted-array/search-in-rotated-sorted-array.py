class Solution:
    def search(self, nums: List[int], target: int) -> int:

        for index,num in enumerate(nums):
            if num == target:
                return index 

        return -1