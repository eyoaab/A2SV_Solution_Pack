class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        best = len(nums)

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] < target:
                left = mid + 1

            elif nums[mid] >= target:
                best = mid
                right  = mid - 1
            

        return best   