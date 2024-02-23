class Solution:
    def helper(self,a,b,opr):
        if opr=='+':
            return a+b
        elif opr=='-':
            return b-a
        elif opr=='*':
            return a*b
        else:
            return int(b/a)  

    def evalRPN(self, tokens: List[str]) -> int:

        stack=[]
        operators=['+','-','*','/']

        for token in tokens:
            if token in operators:
                temp=self.helper(stack.pop(),stack.pop(),token)
                stack.append(temp)
            else:
                stack.append(int(token))

        return stack[-1]            

                 
