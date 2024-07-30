class Solution:
    def minimumDeletions(self, s: str) -> int:
        AllB = 0
        answer = 0
        
        for char in s:
            if char == 'b':
                AllB += 1
            else: 
                answer = min(answer + 1, AllB)
        
        return answer
