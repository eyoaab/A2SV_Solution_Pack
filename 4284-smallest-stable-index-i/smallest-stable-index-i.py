class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        maxl = [0] * n
        maxl[0] = nums[0]

        for i in range(1, n):
            maxl[i] = max(maxl[i - 1], nums[i])

        minr = [0] * n
        minr[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            minr[i] = min(minr[i + 1], nums[i])

        for i in range(n):
            temp = maxl[i] - minr[i]

            if temp <= k:
                return i

        return -1