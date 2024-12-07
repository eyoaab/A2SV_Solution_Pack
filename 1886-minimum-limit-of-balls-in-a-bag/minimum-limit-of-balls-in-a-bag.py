class Solution:
    def minimumSize(self, nums: List[int], k: int) -> int:
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) >> 1
            count = sum(( num - 1) // mid for num in nums)
            if count <= k: 
                right = mid
            else: 
                left = mid + 1

        return right

        