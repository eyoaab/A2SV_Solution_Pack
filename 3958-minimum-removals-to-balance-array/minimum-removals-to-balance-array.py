class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        j = 1
        mini = float('inf')
        
        for i in range(n):
            while j < n and nums[i] * k >= nums[j]:
                j += 1
            ans = i + n - j
            mini = min(mini,ans)
        
        return mini        