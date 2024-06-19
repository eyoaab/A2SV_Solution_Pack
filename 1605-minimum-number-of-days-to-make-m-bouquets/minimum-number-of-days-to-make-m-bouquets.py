class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        val = m * k
        if val > n:
            return -1
        
        low = float('inf')
        high = float('-inf')
        for day in bloomDay:
            low = min(day, low)
            high = max(day, high)
        
        while low <= high:
            mid = low + (high - low) // 2
            if self.possible(bloomDay, mid, m, k):
                high = mid - 1
            else:
                low = mid + 1
        
        return low
    
    def possible(self, bloomDay, day, m, k):
        cnt = 0
        num = 0
        for bd in bloomDay:
            if bd <= day:
                cnt += 1
            else:
                num += cnt // k
                cnt = 0
        num += cnt // k
        return num >= m