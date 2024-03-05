from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(permut):
            if len(permut) == len(nums):
                answer.append(permut.copy())
                return 
            for num in nums:
                if not num in permut:
                    permut.append(num)
                    backtrack(permut)
                    permut.pop()
        answer=[]
        backtrack([])            
                          
        return answer
