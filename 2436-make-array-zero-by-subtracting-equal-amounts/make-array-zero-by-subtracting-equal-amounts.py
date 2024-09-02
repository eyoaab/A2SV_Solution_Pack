class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        length = len(set(nums))

        if 0 in nums:
            return length - 1

        return length    