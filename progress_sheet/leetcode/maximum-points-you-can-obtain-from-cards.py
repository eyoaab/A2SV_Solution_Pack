class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result=0
        for i in range(k):
            result+=cardPoints[i]
        current=result
        for i in range(k-1,-1,-1):
            current-= cardPoints[i]
            current+=cardPoints[len(cardPoints)-k+i]
            result=max(result,current)
        return result       
        