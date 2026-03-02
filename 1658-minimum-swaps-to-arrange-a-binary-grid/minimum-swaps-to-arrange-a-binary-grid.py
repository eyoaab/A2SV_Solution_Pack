class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)

        nums = [0] * n
        for i, row in enumerate(grid):
            cnt = 0
            for x in reversed(row):
                if x == 1:
                    break
                cnt += 1
            nums[i] = cnt
        
        ans = 0
        for k in range(n - 1, 0, -1):
            for x in nums:
                if x >= k:
                    nums.remove(x)
                    break
                ans += 1
            else:
                return -1

        return ans