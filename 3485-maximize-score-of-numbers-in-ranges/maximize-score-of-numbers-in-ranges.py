class Solution:
    def maxPossibleScore(self, start: List[int], d: int) -> int:
        start.sort()
        
        def helper(mid):  
            value = -inf
            for s in start: 
                value += mid
                if value > s + d: 
                    return False 
                value = max(value, s)
            return True 
        
        left, right = 0, 2000000000
        best = 0

        while left <= right: 
            mid = (left + right) // 2
            if helper(mid):
                best = mid
                left = mid + 1
            else: 
                right = mid - 1

        return best 