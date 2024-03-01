class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:(x[0]))
        first=intervals[0][0]
        last=intervals[0][1]
        answer=[]

        for interval in intervals[1:]:
            if interval[0]<=last:
                first=min(first,interval[0])
            else:
                answer.append([first,last])
                first=interval[0] 
            last=max(last,interval[1])
        answer.append([first,last]) 
        return answer         

        