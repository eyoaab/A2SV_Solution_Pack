class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        
        stack=[]
        
        for i in s:
            if stack and i!='(':
                if stack[-1] !='(':
                    val=stack.pop()
                    val*=2
                    stack.pop()
                    while stack and stack[-1]!='(':
                        val+=stack.pop()
                    stack.append(val)
                elif stack[-1]=='(':
                    stack.pop()
                    val=1
                    while stack and stack[-1]!='(':
                        val+=stack.pop()
                    stack.append(val) 
                else:
                    stack.append(i)
            else:
                stack.append(i)

        return stack[-1]                               


        
        
        
        
        
        
        
        
        
        return sum(stack)            




              
        