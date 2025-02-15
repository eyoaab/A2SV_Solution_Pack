class Solution:
    def punishmentNumber(self, n: int) -> int:
        def helper(x, target):
            if x == target: 
                return True 
            if x == 0: 
                return target == 0

            for m in (10, 100, 1000):
                if helper(x // m, target - x % m):
                    return True
                    
            return False
            
        return sum(x for i in range(1, n + 1) if helper( x := i * i, i))
       