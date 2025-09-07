class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        for i in range(n // 2):
            ans.append( i + 1)
            ans.append( -1 * (i + 1))
        
        return ans if len(ans) == n else ans + [0]