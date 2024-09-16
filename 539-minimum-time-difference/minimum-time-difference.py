class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convert_to(time):
            hours, minutes = map(int, time.split(':'))
            return hours * 60 + minutes
        time_point = sorted(convert_to(tp) for tp in timePoints)

      
        answer = float('inf')
        for i in range(len(time_point) - 1):
            temp = time_point[i+1] - time_point[i]
            answer = min(answer, temp)


        curr = (24 * 60) - (time_point[-1] - time_point[0])
        answer = min(answer,curr)

        return answer