class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return 0

        n = len(nums)
        prefix = [0] * (n + 1)
        
        for i, num in enumerate(nums):
            prefix[i + 1] = prefix[i] + 1 if num == target else prefix[i]
        
        res = 0
        for i in range(n):
            for j in range(i, n):
                if 2 * (prefix[j + 1] - prefix[i]) > j - i + 1:
                    res += 1
        
        return res