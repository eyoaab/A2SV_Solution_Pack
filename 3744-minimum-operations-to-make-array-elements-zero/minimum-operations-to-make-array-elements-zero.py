class Solution:
    def helper(self, l: int, r: int) -> int:
        L = 1
        S = 1
        steps = 0
        
        while L <= r:
            R = 4 * L - 1
            start = max(L, l)
            end = min(R, r)
            
            if start <= end:
                steps += (end - start + 1) * S
            
            S += 1
            L *= 4  
            
        return steps

    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            steps = self.helper(l, r)
            res += (steps + 1) // 2 
        return res