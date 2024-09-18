class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        answer = []
        for i in range(0,len(s),k):
            answer.append(s[i:i+k])

        diff = abs(len(answer[-1]) - k)
        
        if len(answer[-1]) != k:
            for i in range(diff):
                answer[-1] += fill 
        return answer
                
            


        