class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack=[]
        N = [i for i in range(1,n+1)]

        for i in range(len(N)):
            if N[i] in target:
                stack.append('Push')
                
            if N[i] not in target:
                flag = False
                for k in range(i+1,len(N)):
                    if N[k] in target:
                        flag = True
                        break
                if flag:
                    stack.append('Push')
                    stack.append('Pop')
                else:
                    return stack
        return stack