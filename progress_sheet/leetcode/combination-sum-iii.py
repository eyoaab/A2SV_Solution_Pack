class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums=[1,2,3,4,5,6,7,8,9]
        answer=[]
    
        
        def backtrack(array,start,_sum):
           

            if len(array)==k and _sum==n:
                answer.append(array[:])
                return
            if start==len(nums) or _sum>n:
                return   
            for i in range(start,9):

                array.append(nums[i])
                backtrack(array,i+1,_sum+nums[i]) 
                array.pop()

        backtrack([],0,0)

        return answer           
        