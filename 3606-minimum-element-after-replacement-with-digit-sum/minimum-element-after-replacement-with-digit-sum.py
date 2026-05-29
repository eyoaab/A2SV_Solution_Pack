class Solution:
    def minElement(self, nums: List[int]) -> int:
        def sumDigit(num):
            sum_ = 0
            for s in str(num):
                sum_ += int(s)
            return sum_

        for i in range(len(nums)):
            nums[i] = sumDigit(nums[i])

        return min(nums)           