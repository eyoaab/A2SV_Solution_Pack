class Solution:
    def maxRunTime(self, n: int, batteries: list[int]) -> int:
        def helper(minutes):
            total = 0
            for battery in batteries:
                total += min(battery, minutes)
            return total >= n * minutes
        
        batteries.sort()
        
        left, right = 0, sum(batteries) // n
        
        while left < right:
            mid = (left + right + 1) // 2
            if helper(mid):
                left = mid 
            else:
                right = mid - 1 
        
        return left