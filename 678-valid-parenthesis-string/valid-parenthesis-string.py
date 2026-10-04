class Solution:
    def checkValidString(self, s: str) -> bool:
        stars = []
        stack = []

        for i,char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                elif stars:
                    stars.pop()
                else:
                    return False
            else:
                stars.append(i)
                
        while stack and stars:
            if stack[-1] > stars[-1]:
                return False        
            stack.pop()
            stars.pop()
    
        return len(stack) == 0    
        