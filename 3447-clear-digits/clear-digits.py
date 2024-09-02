class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for i in s:
            if i.isdigit():
                if stack and not(stack[-1].isdigit()):
                    stack.pop()
                else:
                    stack.append(i)  
            else:
                stack.append(i)

        if stack:
            return ''.join(stack)

        return ''                        