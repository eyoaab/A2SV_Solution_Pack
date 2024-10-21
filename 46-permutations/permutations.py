class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)

        def backtrack(cur, mask):
            if len(cur) == n:
                answer.append(cur[:])
                return
            
            for i in range(n):
                if mask & (1 << i):
                    continue
                
                backtrack(cur + [nums[i]], mask | (1 << i))

        backtrack([], 0)
        return answer
