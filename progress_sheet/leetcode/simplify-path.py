class Solution:
    def simplifyPath(self, path: str) -> str:
        divide = path.split('/')
        stack = []
        for part in divide:
            if part == '..':
                if stack:
                    stack.pop()
            elif part and part != '.':
                stack.append(part)
        return '/' + '/'.join(stack)