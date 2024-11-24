class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0
        min_ = float('inf')
        cnt = 0
        
        for row in matrix:
            for val in row:
                if val < 0:
                    cnt += 1
                min_ = min(abs(val), min_)
                total_sum += abs(val)
        
        if cnt % 2 == 1:
            total_sum -= 2 * min_
        
        return total_sum