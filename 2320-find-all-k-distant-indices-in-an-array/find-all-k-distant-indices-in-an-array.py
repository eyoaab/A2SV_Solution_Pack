class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        keys = [-inf] + [idx for idx, num in enumerate(nums) if num == key] + [inf]
        N = len(nums)
        res = []
        left = 0
        
        for i in range(N):
            if i - keys[left] <= k or keys[left + 1] - i <= k:
                res.append(i)
            if keys[left + 1] == i:
                left += 1
                
        return res