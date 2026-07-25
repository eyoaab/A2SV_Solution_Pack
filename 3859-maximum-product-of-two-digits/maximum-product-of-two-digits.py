class Solution:
    def maxProduct(self, n: int) -> int:
        n_str = list(str(n))
        n_str.sort()
        
        return int(n_str[-1]) * int(n_str[-2])
       
        

        