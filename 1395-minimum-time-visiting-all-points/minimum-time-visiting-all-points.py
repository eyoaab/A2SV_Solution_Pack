class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(1,len(points)):
            a,b =  points[i]
            preva,prevb = points[i -1]
            first,second = abs(a - preva) , abs(b-prevb)

            ans += max(first,second)
        return ans