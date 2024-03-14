class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        answer=0
        a=points[0][0]
        b=points[0][1]

        for point in points[1:]:
            x,y=point
            answer+=max(abs(x-a),abs(y-b))
            a=x
            b=y

        return answer    
        