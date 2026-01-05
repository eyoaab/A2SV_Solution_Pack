class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        ans = 0
        min_ = float('inf')
        cnt = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                min_ = min(abs(val), min_)
                ans += abs(val)
        
        if cnt % 2 == 1:
            ans -= 2 * min_
        
        return ans