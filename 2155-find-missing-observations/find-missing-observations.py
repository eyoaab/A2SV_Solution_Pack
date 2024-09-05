class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        return [] if (miss:=(n+len(rolls))*mean-sum(rolls))>6*n or miss<n else [(miss+n-1)//n]*(r:=miss%n)+[miss//n]*(n-r)
        