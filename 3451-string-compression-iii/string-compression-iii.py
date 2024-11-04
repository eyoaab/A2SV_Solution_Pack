class Solution:
    def compressedString(self, word: str) -> str:
        stack = []
        N = len(word)
        ans = []


        for char in word:
            if not stack:
                stack.append(char)
            elif len(stack) == 9:
                ans.append(str(9))
                ans.append(stack[-1])
                stack = []
                stack.append(char)
            elif stack[-1] == char:
                stack.append(char)
            else:
                ans.append(str(len(stack)))   
                ans.append(stack[-1])
                stack = []
                stack.append(char)

        if stack:
            ans.append(str(len(stack)))  
            ans.append(stack[-1])   

        return ''.join(ans)       

        