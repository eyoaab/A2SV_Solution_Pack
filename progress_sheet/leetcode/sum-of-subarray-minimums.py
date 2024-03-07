class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        n = len(A)
        next_smaller = [n] * n
        prev_smaller = [0] * n   
        ns_s = []
        ps_s = []
        for i, a in enumerate(A):
            while ns_s and A[ns_s[-1]] > a:
                j = ns_s.pop()
                next_smaller[j] = i
            
            ns_s.append(i)
                
            while ps_s and A[ps_s[-1]] > a:
                ps_s.pop()
                
            if ps_s:
                prev_smaller[i] = ps_s[-1]
            else:
                prev_smaller[i] = -1
                
            ps_s.append(i)
        
        res = 0
        for i, a in enumerate(A):
            res += (i - prev_smaller[i]) * a * (next_smaller[i] - i)
            
        return res % (10**9 + 7)