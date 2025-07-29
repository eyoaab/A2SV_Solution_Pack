class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n

        latest = [-1] * 32

        for i in range(n - 1, -1, -1):
            farthest = i 

            for b in range(32):
                if (nums[i] >> b) & 1:
                    latest[b] = i

                if latest[b] != -1:
                    farthest = max(farthest, latest[b])

            result[i] = farthest - i + 1

        return result 