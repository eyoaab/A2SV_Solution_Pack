class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        _max  = max(nums)
        n = len(nums)
        counter = defaultdict(int)
        left = 0
        answer = 0

        for right in range(n):
            counter[nums[right]] += 1
            if counter[_max] >= k:
                while counter[_max] >= k:
                    counter [nums[left]] -= 1
                    left += 1
                    answer += n-right
                                                   
        return answer        
