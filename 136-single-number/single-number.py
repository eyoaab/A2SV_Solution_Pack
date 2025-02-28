class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = nums[-1]

        for num in nums[:-1]:
            xor ^= num

        return xor    

        