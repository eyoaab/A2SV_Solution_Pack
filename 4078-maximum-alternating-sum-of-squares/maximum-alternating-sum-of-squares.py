
class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key=lambda x: x * x)

        ans = 0
        left, right = 0, len(nums) - 1

        while left <= right:
            ans += nums[right] ** 2
            right -= 1

            if left <= right:
                ans -= nums[left] ** 2
                left += 1

        return ans
