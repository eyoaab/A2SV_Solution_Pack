class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        top = 0

        for num in pushed:
            stack.append(num)
            while stack and stack[-1] == popped[top]:
                stack.pop()
                top += 1


        return not stack
        
