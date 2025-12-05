class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        ans = 0
        total = sum(nums)
        cur = 0
        for i in range(len(nums) - 1):
            cur += nums[i]
            total -= nums[i]
            ans += abs(total - cur) % 2 == 0

        return ans