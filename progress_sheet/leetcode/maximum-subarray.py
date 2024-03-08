class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        answer=nums[0]
        cur=0

        for num in nums:
            if cur<0:
                cur=0
            cur+=num
            answer=max(answer,cur)

        return answer        
        