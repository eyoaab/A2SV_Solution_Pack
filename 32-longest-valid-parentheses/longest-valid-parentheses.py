class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_=0
        start=0
        stack=[]
        
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    if stack:
                        max_=max(max_,i-stack[-1])
                    else:
                        max_=max(max_,i-start+1)
                else:
                    start=i+1
        return max_                            