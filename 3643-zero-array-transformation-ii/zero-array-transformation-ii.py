class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        
        def check(k):
            diff = [0] * (n + 1)
            
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val
            
            current = 0
            for i in range(n):
                current += diff[i]
                if current < nums[i]:
                    return False
            
            return True
        
        if all(x == 0 for x in nums):
            return 0
        
        left, right = 1, len(queries)
        
        if not check(right):
            return -1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left