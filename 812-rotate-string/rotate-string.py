class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        li=[]
        for i in s:
            li.append(i)
        for i in range(len(s)):
            if ''.join(li)==goal:
                return True
            else:
                ch=li[0] 
                li.pop(0) 
                li.append(ch) 
        return False  
                 
            
        