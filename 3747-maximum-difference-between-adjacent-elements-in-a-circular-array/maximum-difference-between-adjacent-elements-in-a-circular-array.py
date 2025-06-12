class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            differance = abs(nums[i] - nums[i - 1])
            answer = max(answer,differance)


        return answer