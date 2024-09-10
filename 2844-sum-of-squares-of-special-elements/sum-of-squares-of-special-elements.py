class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        answer = 0
        N = len(nums)

        for index, num in enumerate(nums): 
            if (index + 1 == 1) or (N % (index + 1) == 0):
                answer += num * num

        return answer
