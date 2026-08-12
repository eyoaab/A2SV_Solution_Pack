class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        referance = defaultdict(int)
        answer = 0
        left = 0
        
        for right in range(len(nums)):
            if referance[nums[right]] + 1 >= k:
                while left < right and referance[nums[right]] == k:
                    referance[nums[left]] -= 1
                    left += 1
            
            referance[nums[right]] += 1 
            answer = max(answer,right - left +1)

        return answer            

        