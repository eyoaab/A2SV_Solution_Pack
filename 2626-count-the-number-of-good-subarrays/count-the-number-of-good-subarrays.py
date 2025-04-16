class Solution:
    def countGood(self, nums: List[int], k: int):
        freq = defaultdict(int) 
        left = 0
        pairs = 0
        ans = 0
       
        for right in range(len(nums)):
            val = nums[right]
            pairs += freq[val] 
            freq[val] += 1

          
            while pairs >= k:
                ans += len(nums) - right
                out = nums[left]
                freq[out] -= 1
                pairs -= freq[out]
                left += 1
                
        return ans