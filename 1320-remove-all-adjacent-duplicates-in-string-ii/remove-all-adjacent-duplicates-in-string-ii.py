class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        value = []

        for i in s:
            if stack:
                if stack[-1] == i:
                    value[-1] += 1
                    if value[-1] == k:
                        value.pop()
                        stack.pop()
                else:
                    stack.append(i)
                    value.append(1)
            else:
                stack.append(i)
                value.append(1)          

        answer = ""
        for i in range(len(stack)):
            answer += stack[i] * int(value[i])
        return answer                   