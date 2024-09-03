class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []

        for nu in str(num):

            while k > 0 and stack and int(stack[-1]) > int(nu):
                stack.pop()
                k -= 1

            stack.append(nu) 

        stack = ''.join(stack).lstrip('0') 
        if k > 0:
            stack = stack[:-k]
        if stack:
            return stack
        return '0'         