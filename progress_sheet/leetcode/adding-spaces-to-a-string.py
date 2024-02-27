

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        new=""
        p=0
        for i in range(len(s)):
            if p<len((spaces)) and i==spaces[p]:
                new+=" "
                p+=1
            new+=s[i]    
        return new