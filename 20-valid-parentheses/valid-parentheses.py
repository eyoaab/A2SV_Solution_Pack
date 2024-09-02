class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in '({[':
                stack.append(i)
            else:
                if i == ']':
                    if stack and stack[-1] == '[':
                        stack.pop()
                    else:
                        return False        
                elif i == ')':
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        return False    
                elif i == '}':
                    if stack and stack[-1] == '{':
                        stack.pop()
                    else:
                        return False  
        if stack:
            return False

        return True                                  