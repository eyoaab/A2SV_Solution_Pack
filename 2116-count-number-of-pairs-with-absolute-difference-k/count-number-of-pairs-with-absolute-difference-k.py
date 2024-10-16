class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0

        for i in range(len(nums)):
            for j in range(i +1,len(nums)):
                ans += abs(nums[i] - nums[j]) == k

        return ans        