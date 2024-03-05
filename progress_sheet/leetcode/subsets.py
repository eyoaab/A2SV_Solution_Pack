from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer=[]

        def backtrack(start,sub_set):
            answer.append(sub_set[:])
            
            for i in range(start,len(nums)):
                sub_set.append(nums[i])
                backtrack(i+1,sub_set)
                sub_set.pop()

        backtrack(0,[])

        return answer        
            
                
