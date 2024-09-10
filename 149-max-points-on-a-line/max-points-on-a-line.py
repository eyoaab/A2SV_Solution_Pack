class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        if N == 1: 
            return 1
        answer = 2

        for i in range(N):
            store = defaultdict(int)
            for j in range(N):
                if i != j:
                    store[math.atan2(points[j][1] - points[i][1], points[j][0] - points[i][0])] += 1
            answer = max(answer, max(store.values()) + 1)

        return answer
                    