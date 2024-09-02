class Solution:
    def isValid(self, s: str) -> bool:
        if not (s.count('a') == s.count('b') ==  s.count('c')):
            return False
        stack = []
        for i in s:
            if i != 'c':
                stack.append(i)
            else:
                if len(stack) < 2:
                    return False

                if stack [-1] == 'b':
                    stack.pop()
                    if stack[-1] == 'a':
                        stack.pop()


        if stack:
            return False

        return True                     
                       
