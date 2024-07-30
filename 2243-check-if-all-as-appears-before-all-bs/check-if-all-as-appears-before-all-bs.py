class Solution:
    def checkString(self, s: str) -> bool:
        indexa = float('-inf')
        indexb = float('inf')

        for i in range(len(s)):
            if s[i] == 'a':
                indexa = max(indexa,i)
            else:
                indexb = min(indexb,i)  

        return indexa < indexb          