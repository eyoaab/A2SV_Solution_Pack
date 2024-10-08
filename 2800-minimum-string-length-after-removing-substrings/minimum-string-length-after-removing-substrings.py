class Solution:
    def minLength(self, s: str) -> int:
        stack = []

        for val in s:
            if not stack or (val != 'B' and val != 'D'):
                stack.append(val)
            else:
                if stack[-1] == 'A' and  val == 'B':
                    stack.pop()
                elif stack[-1] == 'C' and val  == 'D':
                    stack.pop()
                else:
                    stack.append(val)
        return len(stack)                
