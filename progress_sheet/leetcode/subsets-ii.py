from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = []
        def backtrack(start, subset):
            answer.append(subset.copy()) 
            for i in range(start, len(nums)):
              
                if i > start and nums[i] == nums[i - 1]:
                   # print("nums[i]", nums[i] )
                    # print("nums[i-1]", nums[i-1] )
                    continue
                subset.append(nums[i])
                backtrack(i + 1, subset)
                subset.pop()

        nums.sort()  
        backtrack(0, [])
        return answer
