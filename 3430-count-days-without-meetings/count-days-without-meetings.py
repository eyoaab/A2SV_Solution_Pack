class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        
        merged = []
        for meeting in meetings:
            if not merged or meeting[0] > merged[-1][1]:
                merged.append(meeting)
            else:
                merged[-1][1] = max(merged[-1][1], meeting[1])
        
        count = 0
        for start, end in merged:
            count += end - start + 1
        
        return days - count
        