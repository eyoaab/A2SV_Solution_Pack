class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        prefix = [0]
        sum_ = 0

        for num in nums:
            sum_ += num
            prefix.append(sum_)



        return max(prefix) - min(prefix) 