class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        for n in nums:
            if not n - 1 in nums:
                length = 1
                while (n + 1) in nums:
                    length += 1
                    n += 1
                res = max(res, length)
        return res