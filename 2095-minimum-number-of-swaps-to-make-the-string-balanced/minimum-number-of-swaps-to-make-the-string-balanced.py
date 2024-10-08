class Solution:
    def minSwaps(self, s: str) -> int:
        stack = []
        s = list(s)
        opens = [i for  i in range(len(s)) if s[i] == '[']
        ans = 0
        
        for i in range(len(s)):
            val =  s[i]
            if val == '[':
                stack.append('[')
            else:
                if stack:
                    stack.pop()
                else:
                    index = opens.pop() 
                    stack.append('[') 
                    s[i],s[index] = s[index],s[i]
                    ans += 1
        return ans        
                    

        