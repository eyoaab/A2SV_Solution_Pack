class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        result = [0 for i in range(n)]
        if k == 0: 
            return result
        if k > 0:
            result[0] = wsum = sum(code[1:k+1])
            for l in range(1, n):
                r = (l+k) % n
                wsum += -code[l] + code[r]
                result[l] = wsum
            return result
        result[0] = wsum = sum(code[-1:k-1:-1])
        
        for l in range(1, n):
            r = (l-k) % n
            wsum += -code[-l] + code[-r]
            result[-l] = wsum

        return result
        
        