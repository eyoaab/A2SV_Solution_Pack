class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)

        intervals = sorted(zip(startTime, endTime))

        gaps = [intervals[0][0]]
        for i in range(1, n):
            gaps.append(intervals[i][0] - intervals[i - 1][1])  
        gaps.append(eventTime - intervals[-1][1])  

        maxBefore = [0] * (n + 2)
        maxAfter = [0] * (n + 2)
        for i in range(1, n + 1):
            maxBefore[i] = max(maxBefore[i - 1], gaps[i - 1])
        for i in range(n, 0, -1):
            maxAfter[i] = max(maxAfter[i + 1], gaps[i])

        maxFree = 0

        for i in range(n):
            duration = intervals[i][1] - intervals[i][0]
            leftGap = gaps[i]
            rightGap = gaps[i + 1]
            combinedGap = leftGap + rightGap

            bestGap = max(maxBefore[i] if i > 0 else 0,
                          maxAfter[i + 2] if i < n - 1 else 0)

            if duration <= bestGap:
                maxFree = max(maxFree, combinedGap + duration)
            else:
                maxFree = max(maxFree, combinedGap)

        for gap in gaps:
            maxFree = max(maxFree, gap)

        return maxFree