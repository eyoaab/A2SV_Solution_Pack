class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if not set(b).issubset(set(a)):
            return -1
        
        answer = ceil(len(b) / len(a))  
     
        repeated = a * answer
        if b in repeated:
            return answer
        elif b in repeated + a:
            return answer + 1
        
        return -1
