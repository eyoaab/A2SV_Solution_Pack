class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        li=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and  stack[-1][-1]< temperatures[i]:
                li[stack[-1][0]]=i-stack[-1][0]
                stack.pop()      
            temp=(i,temperatures[i])
            stack.append(temp)             
        return li