class Solution:
    def minSwaps(self, s: str) -> int:
        stack = 0
        s = list(s)
        opens = [i for  i in range(len(s)) if s[i] == '[']
        ans = 0
        
        for i in range(len(s)):
            val =  s[i]
            if val == '[':
                stack += 1
            else:
                if stack:
                    stack -= 1
                else:
                    index = opens.pop() 
                    stack += 1
                    s[i],s[index] = s[index],s[i]
                    ans += 1
        return ans        
                    

        