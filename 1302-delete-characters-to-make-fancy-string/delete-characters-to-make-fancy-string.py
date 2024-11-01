class Solution:
    def makeFancyString(self, s: str) -> str:
        stack = []

        for char in s:
            if len(stack) < 2:
                stack.append(char)

            elif stack[-1] != char or stack[-2] != char:
                stack.append(char)

        return ''.join(stack)         