class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefixSum = list(accumulate(nums, operator.add))

        dp = [0 for i in range(n)]
        left, right, size = 0, -1, 10**9

        for index, num in enumerate(prefixSum):
            if num >= k:
                size = min(size, index + 1)
            while left <= right and num - prefixSum[dp[left]] >= k:
                size = min(size, index - dp[left])
                left += 1
            while left <= right and num <= prefixSum[dp[right]]:
                right -= 1
            right += 1
            dp[right] = index

        return size if size != 10**9 else -1
        