class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(_sum,array,index):
            if _sum == target:
                answer.append(array[:])
                return

            if index == len(candidates) or _sum>target:
                return 
                
            array.append(candidates[index])
            backtrack(_sum+candidates[index],array,index)
            
            array.pop()
            backtrack(_sum,array,index+1)


        candidates.sort() 
        backtrack(0, [], 0)
        return answer
