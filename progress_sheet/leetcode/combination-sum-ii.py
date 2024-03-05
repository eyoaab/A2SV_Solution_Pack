class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(_sum,array,index):
            if _sum == target:
                answer.append(array[:])
                return
            if index == len(candidates) or _sum>target:
                return 

            for i in range(index,len(candidates)):
                if i>index and candidates[i] == candidates[i-1]:
                    continue  
                array.append(candidates[i])
                backtrack(_sum+candidates[i],array,i+1)
                array.pop()

        candidates.sort() 
        backtrack(0, [], 0)
        return answer