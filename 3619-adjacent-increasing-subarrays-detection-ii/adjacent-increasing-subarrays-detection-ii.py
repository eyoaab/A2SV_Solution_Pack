class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n, count, prev, k = len(nums), 1, 0, 0

        for i in range(1, n):
            if nums[i] > nums[i-1]: 
                count += 1
            else:
                k = max(k, count//2, min(count, prev))
                prev = count
                count = 1
        
        return max(k, count // 2, min(count, prev))
        