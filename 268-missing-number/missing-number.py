class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        nums.sort()
        best = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > mid:
                right = mid - 1
                best = mid
            else:
                left = mid  + 1

        return best           
