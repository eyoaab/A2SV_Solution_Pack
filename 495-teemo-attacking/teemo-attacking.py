class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        answer = duration

        for i in range(1,len(timeSeries)):
            answer += min(timeSeries[i] - timeSeries[i - 1],duration)

        return answer    