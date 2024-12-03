

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = ""
        N = len(s)
        p = 0
        for i in range(N):
            if p < len((spaces)) and i == spaces[p]:
                answer += " "
                p += 1
            answer += s[i]    
            
        return answer