class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        mini = nums[0]
        answer = 0

        for i in range(1,len(nums)):
            answer = max(answer,nums[i] - mini)
            mini = min(nums[i] , mini)  

        return answer if answer != 0 else -1    