class Solution:
    def alternatingSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        maxi = 0

        for i in range(n - 1):
            if nums[i+1] != nums[i] + 1:
                continue
            curr, prev = 2, 1
            for j in range(i + 2, n):
                diff = nums[j] - nums[j-1]
                if diff == -prev:
                    curr += 1
                    prev = -prev
                else:
                    break
            maxi = max(maxi, curr)
            
        return maxi if maxi > 0 else -1